import cv2
import dropbox
import time
import random

starttime=time.time()
def takesnapshot():
    num=random.randint(0, 100)
    vco=cv2.VideoCapture(0)
    result=True
    while(result):
        r, frame=vco.read()
        filename="img"+str(num)+'.png'
        cv2.imwrite(filename, frame)
        starttime=time.time()
        result=False
    return filename
    print("Snapshot taken")
    vco.release()
    cv2.destroyAllWindows()

def uploadfile(source):
    accesstoken=''
    file=source
    destination="/Backup/"+file
    dbx= dropbox.Dropbox(accesstoken)
    with open(source, 'rb') as f:
        dbx.files_upload(f.read(), destination, mode=dropbox.files.WriteMode.overwrite)
        print("Fileuploaded")

while(True):
    if(time.time()-starttime)>=5:
        name=takesnapshot()
        uploadfile(name)
