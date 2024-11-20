import os
import shutil

def organize_files_by_type(directory_path):
    """
    Organizes files in the specified directory by their file extensions (types).
    Moves the files into folders named after their extension type.
    
    Parameters:
    directory_path (str): The path to the directory containing files to organize.
    """

    if not os.path.exists(directory_path):
        print(f"The specified directory '{directory_path}' does not exist.")
        return
    
    os.chdir(directory_path)

    files = [f for f in os.listdir() if os.path.isfile(f)]
    
    for file in files:
       
        file_extension = file.split('.')[-1]
        destination_folder = os.path.join(directory_path, file_extension.upper())  

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder) 

        
        try:
            shutil.move(file, os.path.join(destination_folder, file))
            print(f"Moved '{file}' to '{destination_folder}'")
        except Exception as e:
            print(f"Error moving {file}: {e}")


directory_to_organize = r'C:/Users/SEC/Documents' 
organize_files_by_type(directory_to_organize)
