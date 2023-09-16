import os
import shutil

# Get the directory where the script is located
script_directory = os.path.dirname(__file__)

# Change the current working directory to the script's directory
os.chdir(script_directory)

# List files in the current directory
files = os.listdir()

# Dictionary of extensions and their corresponding directories
extensions = {
    "images": [".jpg", ".png", ".jpeg", ".gif"],
    "videos": [".mp4", ".mkv"],
    "musics": [".mp3", ".wav"],
    "zip": [".zip", ".tgz", ".rar", ".tar"],
    "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls", ".txt"],
    "setup": [".msi", ".exe"],
    "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP"],
    "design": [".xd", ".psd"]
}

# Function to determine the category of a file based on its extension
def sort_file(file):
    for category, ext_list in extensions.items():
        for ext in ext_list:
            if file.endswith(ext):
                return category
    return "others"

# Iterate through each file and move it to the appropriate directory
for file in files:
    if os.path.isfile(file):  # Check if it's a file (not a directory)
        category = sort_file(file)
        destination_dir = os.path.join(script_directory, category)
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        destination_path = os.path.join(destination_dir, file)
        if not os.path.exists(destination_path):
            shutil.move(file, destination_path)
        else:
            print(f"{file} already exists in {category}")
