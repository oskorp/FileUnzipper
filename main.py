import zipfile

target = "new.zip"

print('Chaliye shuru karte hai.....')


root=zipfile.ZipFile(target)

root.extractall('file')
root.close()


print('Chalo hogaya khatam')