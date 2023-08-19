import os
import shutil

# Source directory containing YAML files
source_directory = '/home/alvin/Desktop/cent-nuclei-templates'

# Destination directory where YAML files will be moved
destination_directory = '/home/alvin/Desktop/alvin/nuclei-templates/my-nuclei-templates'

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Iterate through the source directory
for root, dirs, files in os.walk(source_directory):
    for file in files:
        if file.endswith('.yaml') or file.endswith('.yml'):  # Check if it's a YAML file
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_directory, file)
            
            # Move the file to the destination directory
            shutil.move(source_path, destination_path)
            
            print(f"Moved {file} to {destination_directory}")

print("All YAML files have been moved.")
