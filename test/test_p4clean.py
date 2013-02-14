import pytest
import shutil
import os
import p4clean


def test_delete_empty_folders():
    root_folder = os.tmpnam()

    # Create a folder tree
    os.mkdir(root_folder)
    os.mkdir(root_folder + '/folderA')
    os.mkdir(root_folder + '/folderA/folderAA')
    os.mkdir(root_folder + '/folderB')
    os.mkdir(root_folder + '/folderC')
    os.mkdir(root_folder + '/folderC/folderCC')
    os.mkdir(root_folder + '/folderD')
    os.mkdir(root_folder + '/folderD/folderDD')

    def create_file(root, path):
        temp_file_path = root + '/' + path
        temp_file = open(temp_file_path, "wb")
        temp_file.write("")
        temp_file.close()

    # populate random folders with one file
    create_file(root_folder, 'folderA/temp.txt')
    create_file(root_folder, 'folderA/folderAA/temp.txt')
    create_file(root_folder, 'folderD/folderDD/temp.txt')

    # the tested function call
    p4clean.delete_empty_folders(root_folder)

    folder_list = [path for path, directories, files in os.walk(root_folder)]

    assert root_folder in folder_list, "Folder is not empty and should still  exist"
    assert root_folder + '/folderA' in folder_list, "Folder is not empty and should still  exist"
    assert root_folder + '/folderA/folderAA' in folder_list, "Folder is not empty and should still  exist"
    assert root_folder + '/folderD' in folder_list, "Folder is not empty and should still  exist"
    assert root_folder + '/folderD/folderDD' in folder_list, "Folder is not empty and should still  exist"
    assert root_folder + '/folderB' not in folder_list, "Folder is empty and should not exist"
    assert root_folder + '/folderC' not in folder_list, "Folder is empty and should not exist"
    assert root_folder + '/folderC/folderCC' not in folder_list, "Folder is empty and should not exist"

    shutil.rmtree(root_folder)


pytest.main()
