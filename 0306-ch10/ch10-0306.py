#Q3
def WriteInfo(File,Info):
    try:
        f = open(File,'a')
        f.write(Info+'\n')
        f.close()
        return True
    except Exception:
        return False

def GetInfo():
    InfoList = open(r'ch10-0306-related\File1.txt','r').readlines()+open(r'ch10-0306-related\File2.txt','r').readlines()
    ID_List , NameList = [],[]
    for IF in InfoList:
        count = 0
        while count<len(IF):
            if IF[count] == '*':
                break
            count+=1
        ID_List.append(IF[:count])
        NameList.append(IF[count+1:-2])
    while True:
        ID = input('ID (One upper case aplhpabetic character followed by four numbers): ')
        check = True
        if 65 <= ord(ID[0]) <= 90:
            if len(ID) == 5:
                for i in range(1,4):
                    if not 48 <= ord(ID[i]) <= 57:
                        check = False
                if not ID in ID_List and check:
                    break
        print('Invalid or used ID!')
    Name = input('Name: ')
    return ID+'*'+Name

def TopLevel():
    while True:
        Info = GetInfo()
        if 65 <= ord(Info[0]) <= 77:
            File = r'ch10-0306-related\File1.txt'
        else:
            File = r'ch10-0306-related\File2.txt' 
        Flag = WriteInfo(File,Info)
        if not Flag:
            print('Error occurs when writing file!')
            input()
            break
        Choice = input('Continue? (Y/N)')
        if not Choice == 'Y':
            break



if __name__ == "__main__":
    TopLevel()
