import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for fname in files:
                local_path = os.path.join(root, fname)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path)
    
def main():
    access_token = 'sl.BEQOcAoXhNJEoUmGQYFhA_LEb_voSTU7GeG_9iFOHe0P3EbKl9R8iAnzLDc3qmWzfx6Bz8WvyblcoWPaz5G0LfimqTJg5LNbtaK6fNsTCoFoOvKQ8jHvzrqVMaCupqMo7wqzTbp-'
    transferData = TransferData(access_token)
    file_from = input("Enter the path to the folder: ")
    file_to = input("Enter the path where the file is to be transfered: ")
    transferData.upload_files(file_from, file_to)
    print("Folder uploaded!!")

main()