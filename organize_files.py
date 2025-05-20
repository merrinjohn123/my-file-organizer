mport os
import shutil

folder_path = "/Users/merrinjohn/Downloads"
files = os.listdir(folder_path)

file_types = {
    'Images' : ['.jpg'],
    'Documents' : ['.docx','.pdf','.xlsx'],
    'Videos' : ['.mp4'],
    'Archives' : ['.zip']
}

for filename in files:
    filepath = os.path.join(folder_path,filename)

    if os.path.isfile(filepath):
        ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder,extentions in file_types.items():
            if ext in extentions:
                target_folder = os.path.join(folder_path,folder)
                os.makedirs(target_folder,exist_ok=True)
                shutil.move(filepath,os.path.join(target_folder,filename))
                print(f"Moved {filename} to {folder}")
                moved = True
                break
