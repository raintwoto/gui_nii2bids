# gui_nii2bids
convert your nii file to the bids format



Pre-1. Scan and get your fMRI data.
        
        
1.  Preprocessing
    * Using dcm2nii (or dcm2niigui) to convert your fMRI images to nii file
![gif2](https://user-images.githubusercontent.com/2226218/37960779-c7700654-31b6-11e8-82f3-643aa82ca4ab.gif)

2.  Set-up
    * Download the zip file or git clone the repo

    * Change the "gui_nii2bids_config"
        *  project_path gives you output path  
        *  Types of task are the tasks in your experiment. 'Anat' and 'None' is the default name for Anatomical scans and other scans(not included in the analysis, e.g. the head localizer) 
        <img width="315" alt="nii2bids" src="https://user-images.githubusercontent.com/2226218/37958721-81beaf3e-31b1-11e8-9c80-8d04b585aa13.png">
        
3. Run the code
    * In Linux, you can just run /bin/gui_nii2bids
    
![gif](https://user-images.githubusercontent.com/2226218/37960476-086a60ba-31b6-11e8-932a-f34db3c62d9a.gif)


4. And check your folder
![gif3](https://user-images.githubusercontent.com/2226218/37960929-2f07bf64-31b7-11e8-8ca6-bb78203a500a.gif)
