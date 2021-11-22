import dropbox
import os
from dropbox.files import WriteMode
class Transferdata: 
    def __init__(self, accesstoken):
        self.accesstoken=accesstoken
    def uploadfile(self, source, destination):
        dbx= dropbox.Dropbox(self.accesstoken)
        for root, dirs, files in os.walk(source):
            for filename in files:
                localpath= os.path.join(root, filename)
                relativepath= os.path.relpath(localpath, source)
                dropboxpath= os.path.join(destination, relativepath)
                with open(localpath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxpath, mode=dropbox.files.WriteMode.overwrite)
def main():
    accesstoken=''
    td=Transferdata(accesstoken)
    filefrom = 'D:/AISN/WhitehatJr/Python'
    fileto = '/Backup/'
    while(True):
    if(time.time()-starttime)>=86400:
        td.uploadfile(filefrom, fileto)
        print("Files have been moved")
main()
