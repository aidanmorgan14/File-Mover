import os
import glob
import shutil

# Get the folder path from input
folder_path = r""
destination_folder = r""
keywords = ['syndication', 'ACS Financial', 'T&R']
iteration = 0

# Make sure paths dont end in backslash bc dont work
if folder_path.endswith("\\") or folder_path.endswith("/"):
    folder_path = folder_path[:-1]

if destination_folder.endswith("\\") or destination_folder.endswith("/"):
    destination_folder = destination_folder[:-1]

# Ensure destination folder exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Iterate for the number of metrics needed
for i in keywords:
    keyword = keywords[iteration]
    print(keyword)
    
    # Identify keyword and set appropriate filename/extension
    if keyword == "syndication":
        new_file_name = "Syndications_Data.xlsx"
    elif keyword == "ACS Financial":
        new_file_name = "ACS Financial Data.pdf"
    elif keyword == "T&R":
        new_file_name = "T&R Data.xlsx"

    # Search for files containing the keyword in their names
    search_pattern = os.path.join(folder_path, f"*{keyword}*")
    matching_files = glob.glob(search_pattern)

    # If matching files are found, rename the first one
    if matching_files:
        old_file_path = matching_files[0]
        new_file_path = os.path.join(folder_path, new_file_name)
        
        try:
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{os.path.basename(old_file_path)}' to '{new_file_name}'")
            
            # Move the file to the destination folder and replace if it already exists
            destination_file_path = os.path.join(destination_folder, new_file_name)
            shutil.move(new_file_path, destination_file_path)
            print(f"Moved '{new_file_name}' to '{destination_folder}'")
        except PermissionError:
            print(f"Permission denied when renaming '{os.path.basename(old_file_path)}' or moving '{new_file_name}'")
        except Exception as e:
            print(f"Failed to rename '{os.path.basename(old_file_path)}' or move '{new_file_name}': {e}")
    else:
        print(f"No files found with keyword '{keyword}' in '{folder_path}'")
    iteration += 1

