#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# AHernandez, 2021-Feb-13, Modified File and added requirements from assignment
#------------------------------------------#

# Declare variabls
import pathlib 
 
strChoice = '' # User input
lstTbl = []
dicRow = {}  # dic of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
# Get user Input
print('The Magic CD Inventory\n')
while True:

    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        break

    if strChoice == 'l':
        file = pathlib.Path(strFileName)
        if file.exists():
            lstTbl.clear()
            objFile = open(strFileName, 'r')
            for item in objFile:
                lstRow = item.strip().split(',')
                dicRow = {'ID':lstRow[0],'Title':lstRow[1],'Artist':lstRow[2]}
                lstTbl.append(dicRow)
            objFile.close()
            print('Here is the current CD Inventory:')
            print('ID, CD Title, Artist')
            for row in lstTbl:
                print(*row.values(), sep = ',')
            print('\n') 
        else:
            print('The File {} does not exists!'.format(strFileName))
            print('\n') 
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID':intID, 'Title': strTitle, 'Artist':strArtist}
        lstTbl.append(dicRow)
        print('\n')
        
    elif strChoice == 'i':
        if not lstTbl:
            print('The Inventory is currently empty \n')
        elif lstTbl:
            print('Here is the current CD Inventory:')
            print('ID, CD Title, Artist')
            for row in lstTbl:
                print(*row.values(), sep = ',')
        print('\n') 
        
    elif strChoice == 'd':
        print('This is the current CD Inventory')
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ',')        
        CDDelete = int(input('Which CD Id would you like to remove from the list? ').strip())
        print('\n') 
        rowNu = -1
        for item in lstTbl:
            rowNu += 1
            if int(item['ID']) == CDDelete:
                del lstTbl[rowNu]
                break
        
    elif strChoice == 's':
        objFile = open(strFileName, 'w')
        strRow = ''
        for row in lstTbl:
            for val in row.values():
                strRow += str(val) + ','
            strRow = strRow[:-1] + '\n'
        objFile.write(strRow)
        objFile.close()
        
    else:
        print('Please choose either l, a, i, d, s or x! \n')


