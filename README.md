```markdown
# YAML File Mover Script

This Python script moves YAML files from a source directory to a destination directory.

## Usage

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd yaml-file-mover
   ```

2. **Modify Paths**:
   - Open `move_yaml_files.py` in a text editor.
   - Replace `source_directory` with the path to your source directory containing YAML files.
   - Replace `destination_directory` with the path to your destination directory.
   - Save the file.

3. **Run the Script**:
   - Open a terminal and navigate to the repository's directory.
   - Run the script using the command:
     ```bash
     python move_yaml_files.py
     ```
   - The script will move YAML files from the source directory to the destination directory.

## Script

```python
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
```

---

Please replace the `<repository-url>` placeholder with the actual URL of your GitHub repository. Modify the paths in the script to match your source and destination directories. Review and test the script on your system before running it on important data.

This is the complete README with detailed steps and the script for reference.
