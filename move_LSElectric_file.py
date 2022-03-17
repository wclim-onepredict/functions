import os
import shutil


if __name__ == "__main__":
    print(os.path.abspath(__file__))
    dir_path = "C:\\Users\\luc29\\Desktop\\LS-02-B02E"
    folder_list = os.listdir(path=dir_path)
    for folder in folder_list:
        files_path = os.path.join(dir_path, folder)
        file_list = os.listdir(path=files_path)
        for file_name in file_list:
            if file_name == 'Raw':
                raw_folder_path = os.path.join(files_path, file_name)
                raw_file_list = os.listdir(path=raw_folder_path)
                for raw_file_name in raw_file_list:
                    raw_file_path = os.path.join(raw_folder_path, raw_file_name)
                    src = raw_file_path
                    dir = os.path.join(files_path, raw_file_name)
                    shutil.move(src, dir)
            else:
                pass

            dir_path_raw = files_path + '\\Raw'
            dir_path_rawdata = files_path + '\\RawData'
            if os.path.exists(dir_path_raw):
                os.rmdir(dir_path_raw)
            if os.path.exists(dir_path_rawdata):
                os.rmdir(dir_path_rawdata)
            
        print(f"#### {folder} is done.")
    pass
