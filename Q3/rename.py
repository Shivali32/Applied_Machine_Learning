import os

def rename_images_in_folder(folder_path, label):
    """
    Rename all images in the folder to a sequential format (label_001.jpg, label_002.jpg, etc.)
    """
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist!")
        return

    # Get all files in the directory
    files = os.listdir(folder_path)
    
    # Filter for image files (you can add more extensions if needed)
    image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    # Sort the files to ensure consistent renaming
    image_files.sort()
    
    # Rename files sequentially
    for i, old_name in enumerate(image_files, start=1):
        # Construct the new filename with leading zeros (e.g., 'tulip_001.jpg')
        new_name = f"{label}_{i:03d}{os.path.splitext(old_name)[1]}"
        
        # Construct full paths
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed '{old_name}' to '{new_name}'")

def rename_images_in_dataset(base_folder):
    """
    Rename images in the 'tulip' and 'sunflower' folders under the provided base directory.
    """
    # Path to the tulip and sunflower folders
    tulip_folder = os.path.join(base_folder, 'tulip')
    sunflower_folder = os.path.join(base_folder, 'sunflower')
    
    # Rename images in both folders
    rename_images_in_folder(tulip_folder, 'tulip')
    rename_images_in_folder(sunflower_folder, 'sunflower')

# Use the current working directory if your dataset is in the same directory as the script
# dataset_path = 'flowers'  # Relative path to the flowers folder
dataset_path = "C:/Users/shiva/OneDrive/Desktop/AML/Q3/flowers"  # Relative path to the flowers folder

# Check if the folder exists before proceeding
if os.path.exists(dataset_path):
    rename_images_in_dataset(dataset_path)
else:
    print(f"Dataset folder '{dataset_path}' not found. Make sure it exists in the current directory.")
