import dropbox

class UploadData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token='cMY259YbzKIAAAAAAAAAATZLycEmsCVlIzGjrrmrtbe1Uc2VMdB7-vEhI-BtsRBa'
    transferData=UploadData(access_token)
    file_from='TestFile1.txt'
    file_to='/MyFolder/TestFile1.txt'
    transferData.upload_file(file_from,file_to)
    print('The file has been moved')
main()

