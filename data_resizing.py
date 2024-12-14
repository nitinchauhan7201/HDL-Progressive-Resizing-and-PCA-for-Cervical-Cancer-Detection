# -*- coding: utf-8 -*-
"""data_resizing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MhnWZdXEIuP9yqPTFXMxHX6h2H6MB1dL
"""

import os
import subprocess
import shutil

# Check if Git is installed
if shutil.which("git") is None:
    raise EnvironmentError("Git is not installed or not found in the system PATH. Please install Git and try again.")

# Clone the repository using subprocess
repo_url = 'https://github.com/GotG/object_detection_demo_flow'
repo_name = 'object_detection_demo_flow'
repo_dir_path = os.path.join(os.getcwd(), repo_name)

# Check if the repository already exists to avoid cloning multiple times
if not os.path.exists(repo_dir_path):
    print(f"Cloning repository from {repo_url}...")
    subprocess.run(["git", "clone", repo_url], check=True)
else:
    print(f"Repository {repo_name} already exists.")

# Change directory to the cloned repository
os.chdir(repo_dir_path)

# Pull the latest changes from the repository
print("Pulling the latest changes...")
subprocess.run(["git", "pull"], check=True)

# Define source directory
source_base_dir = r'C:\Users\nitin\Desktop\Cervical_Cancer_Detection\SIPaKMeD'

# Define target sizes and corresponding directories
resize_options = {
    "(224,224)": r'C:\Users\nitin\Desktop\Cervical_Cancer_Detection\SIPaKMeD_224x224',
    "(512,512)": r'C:\Users\nitin\Desktop\Cervical_Cancer_Detection\SIPaKMeD_512x512',
    "(1024,1024)": r'C:\Users\nitin\Desktop\Cervical_Cancer_Detection\SIPaKMeD_1024x1024'
}

# List of subdirectories in SIPaKMeD to be resized
subdirectories = [
    'im_Superficial-Intermediate',
    'im_Parabasal',
    'im_Metaplastic',
    'im_Koilocytotic',
    'im_Dyskeratotic'
]

# Iterate over each target size and directory
for target_size, target_base_dir in resize_options.items():
    for subdirectory in subdirectories:
        raw_dir = os.path.join(source_base_dir, subdirectory)
        save_dir = os.path.join(target_base_dir, subdirectory)

        # Ensure the save directory exists
        os.makedirs(save_dir, exist_ok=True)

        # Construct the command to run the resize script
        command = [
            'python', 'resize_images.py',
            '--raw-dir', raw_dir,
            '--save-dir', save_dir,
            '--ext', 'bmp',
            '--target-size', target_size
        ]

        # Run the command
        print(f"Resizing images in {raw_dir} to {target_size} and saving to {save_dir}...")
        subprocess.run(command, check=True)

print("Image resizing to all sizes completed.")