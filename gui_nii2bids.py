#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 00:11:21 2017
GUI version 2 BIDs
@author: biahan
"""

from Tkinter import *
import Tkinter
import Tkconstants
import tkFileDialog
import os
from shutil import *

f1 = open('./gui_nii2bids_config', 'r').read()
exec(f1)


# %%
master = Tk()
master.directory = tkFileDialog.askdirectory(title = "where is your nii files?")
master.destroy()
files = os.listdir(master.directory)
fmri_file = []
fmri_filedir = []
fmri_filesize = []
for file in files:
    tmp = file
    file = master.directory+'/'+file
    if os.path.isfile(file):
        file_info = os.stat(file)
        if file_info.st_size > 2*1000*1000:  # bigger than 2M
            fmri_file.append(tmp.replace('.nii.gz', ''))
            fmri_filedir.append(file)
            fmri_filesize.append(file_info.st_size/(1000*1000))
#%%
subj_num = []


def spinbox_num():
    subj_num.append(var.get())
    master.destroy()


master = Tk()
Label(master, text='The number of the subject:').grid(row=0, column=0)
var = StringVar(master)
var.set("0")
sb = Spinbox(master, from_=0, to=28, textvariable=var).grid(row=0, column=1)
Button(master, text='Confirm', command=spinbox_num).grid(
    row=1, column=1, sticky=W, pady=4)


mainloop()


#%%
Type = []
Session = []

fmri_filetype = []
fmri_filesession = []
master = Tk()

Label(master, text='Name').grid(row=0, column=0)
Label(master, text='Size').grid(row=0, column=1)
Label(master, text='Type').grid(row=0, column=2)
Label(master, text='Session').grid(row=0, column=3)


def show_entry_fields():
    for ii in range(len(Type)):
        fmri_filetype.append(Type[ii].get())
        fmri_filesession.append(Session[ii].get())
    master.destroy()


for i in range(len(fmri_file)):
    Label(master, text=fmri_file[i]).grid(row=i+1, column=0)
    Label(master, text=str(fmri_filesize[i])+'MB').grid(row=i+1, column=1)
    v = StringVar()
    v.set('None')
    eval("OptionMenu(master,v,"+type_of_task_text+").grid(row=i+1,column=2)")
    Type.append(v)
    myvar = StringVar()
    Entry(master, textvariable=myvar).grid(row=i+1, column=3)
    Session.append(myvar)

Button(master, text='Confirm', command=show_entry_fields).grid(
    row=i+2, column=1, sticky=W, pady=4)

mainloop()
#%%

subj_num = subj_num[0]

#%% Need to be changed
for i in range(len(fmri_filetype)):
    if fmri_filetype[i] == 'Anat':
        if not os.path.exists(project_path+'/data/sub-'+subj_num+'/anat'):
            os.makedirs(project_path+'/data/sub-'+subj_num+'/anat')
        copy2(fmri_filedir[i], project_path+'/data/sub-' +
              subj_num+'/anat/'+'sub-'+subj_num+'_T1w.nii.gz')
    elif fmri_filetype[i] == 'None':
        1
    else:
        if not os.path.exists(project_path+'/data/sub-'+subj_num+'/func'):
            os.makedirs(project_path+'/data/sub-'+subj_num+'/func')
        copy2(fmri_filedir[i], project_path+'/data/sub-'+subj_num+'/func/'+'sub-' +
              subj_num+'_'+fmri_filetype[i]+'-'+fmri_filesession[i]+'_bold.nii.gz')
