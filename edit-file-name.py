import os

def replace_in_filename(folder_path, search_str, replace_str):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if search_str in filename:
                new_filename = filename.replace(search_str, replace_str)
                old_file_path = os.path.join(root, filename)
                new_file_path = os.path.join(root, new_filename)
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")

        for dirname in dirs:
            if search_str in dirname:
                new_dirname = dirname.replace(search_str, replace_str)
                old_dir_path = os.path.join(root, dirname)
                new_dir_path = os.path.join(root, new_dirname)
                os.rename(old_dir_path, new_dir_path)
                print(f"Renamed folder: {old_dir_path} -> {new_dir_path}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    search_str = input("Enter search string: ")
    replace_str = input("Enter replace string: ")
    replace_in_filename(folder_path, search_str, replace_str)