import os #work with files
import shutil #move files
import datetime

downloads = "C:/Users/ayesh/Downloads"
#this is just a path to all downloads

folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "PDFs": [".pdf"],
    "Documents": [".doc", ".docx", ".txt"],
    "Installers": [".exe", ".msi"],
    "Zips": [".zip", ".rar", ".7z"],
}
#dictionary organizing different types of files


for filename in os.listdir(downloads):
    filepath= os.path.join(downloads, filename)

    if os.path.isfile(filepath) and filename != "sorter_log.txt":
        ending= os.path.splitext(filename)[1].lower()
        
        for folder_name, endings in folders.items():
            if ending in endings:
                folder_path = os.path.join(downloads, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(filepath, folder_path)
                log_entry = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} | {filename} - {folder_name}\n"  # added
                print(log_entry.strip())  
                with open(os.path.join(downloads, "sorter_log.txt"), "a") as log:  # added
                    log.write(log_entry)  
                break

print("Downloads folder cleaned!")


