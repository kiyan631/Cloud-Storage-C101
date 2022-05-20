import dropbox

class TransferData : 
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_files(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        with open(file_from,"rb") as f:
           dbx.files_upload(f.read(),file_to)

def main():
   access_token='sl.BHsPCAJ5ObVaA0daDkqeVHzYvWo2J51YF5UHa32sF8mCWWpORw_oyuktTdLK3mDvdgCLKOI6Rg4eMz8xyscQ2jZs0eO4dzbvv5lklPVAr9VpYD7LcJqx5hgt612g3kVQx5wiM00'
   transferData=TransferData(access_token)

   file_from=input('enter the file path to transfer: ')
   file_to=input('enter the full path to upload to dropbox:')

   transferData.upload_files(file_from,file_to)
   print('file has been moved')

main()

