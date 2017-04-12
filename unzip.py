from zipfile import ZipFile

zipFileName = "hello.zip"
dictionary = "dictionary.txt"
status = 'Password not found...\n'

zf = ZipFile(zipFileName)

print("Checking...\n")

with open(dictionary, 'r') as dict:
    for potentialPWDs in dict.readlines():
        potentialPWD = potentialPWDs.strip('\n')
        try:
            print("Trying... %s") % potentialPWD
            zf.extractall(pwd=potentialPWD)
            status = 'Found! Password: %s' % potentialPWD
            break
        except:
            pass
print(str(status))
    
        
