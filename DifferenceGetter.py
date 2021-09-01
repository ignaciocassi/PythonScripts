import os

#For every line in unnormalizedFileADirectory, normalizes it, and writes it to normalizedFileADirectory
def normalizeInputFileA(unnormalizedFileADirectory,normalizedFilaADirectory):
    try:
        inputFile = open(unnormalizedFileADirectory,"rt")
        outputFile = open(normalizedFilaADirectory,"wt")
        inputLine = inputFile.readline()
        while inputLine:
            normalizedItemName = getItemNameA(inputLine)
            outputFile.write(normalizedItemName+"\n")
            inputLine = inputFile.readline()
    except IOError:
        print("Error")
    finally:
        try:
            inputFile.close()
            outputFile.close()
        except:
            pass

#Normalizes the current itemName
def getItemNameA(inputLine):
    normalizedInputLine = inputLine.rstrip("\n")
    normalizedInputLine = normalizedInputLine.replace('"',"")
    fields = normalizedInputLine.split(",")
    blankItem = lambda x : True if (x != "") else False
    fields = list(filter(blankItem, fields))
    itemName = fields[1]
    #lista = itemName.split("(")
    #if (len(lista)>1):
    #    lista = lista[0:-1]
    #itemName = itemName.join(lista)
    itemName = itemName.rstrip(" ")
    #itemName = itemName.replace('(',"")
    #itemName = itemName.replace(')',"")
    itemName = itemName.replace('.',"")
    itemName = itemName.replace("Ã‘","N")
    return itemName

def normalizeInputFileB(unnormalizedFileBDirectory,normalizedFileBDirectory):
    try:
        inputFile = open(unnormalizedFileBDirectory,"rt")
        outputFile = open(normalizedFileBDirectory,"wt")
        inputLine = inputFile.readline()
        while inputLine:
            normalizedItemName = getItemNameB(inputLine)
            outputFile.write(normalizedItemName+"\n")
            inputLine = inputFile.readline()
    except IOError:
        print("Error")
    finally:
        try:
            inputFile.close()
            outputFile.close()
        except:
            pass

def getItemNameB(inputLine):
    fields = inputLine.split(",")
    itemName = fields[0]
    itemName = itemName.replace("ï»¿","")
    itemName = itemName.replace("Ã‘","N")
    itemName = itemName.replace('.',"")
    itemName = itemName.replace('"',"")
    normalizedItemNameB = itemName
    return normalizedItemNameB

def getDifference(normalizedFilaADirectory,normalizedFileBDirectory,differenceFileDirectory):
    try:
        fileA = open(normalizedFilaADirectory,"rt")
        fileB = open(normalizedFileBDirectory,"rt")
        differenceFile = open(differenceFileDirectory,"wt")

        itemA = fileA.readline()
        listItemsA = list()
        while (itemA):
            listItemsA.append(itemA)
            itemA = fileA.readline()
        print("ListItemsA: "+str(len(listItemsA)))

        itemB = fileB.readline()
        listItemsB = list()
        while (itemB):
            listItemsB.append(itemB)
            itemB = fileB.readline()
        print("ListItemsB: "+str(len(listItemsB)))

        for itemA in listItemsA:
            if itemA in listItemsB:
                listItemsA.remove(itemA)
        print("ListItemsA: "+str(len(listItemsA)))

        for item in listItemsA:
            differenceFile.write(item)
    except IOError:
        print("Error")
    finally:
        try:
            fileA.close()
            fileB.close()
            differenceFile.close()
        except:
            pass

def getSortedFileA(directory,sortedDirectory):
    lines = list()
    try:
        file = open(directory,"rt")
        line = file.readline()
        while line:
            lines.append(line)
            line = file.readline()
    except IOError:
        print("Error")
    finally:
        try:
            file.close()
        except:
            pass
    try:
        file = open(sortedDirectory,"wt")
        lines.sort()
        for line in lines:
            file.write(line)

    except IOError:
        print("Error")
    finally:
        try:
            file.close()
        except:
            pass
    
    

def __main__():
    unnormalizedFileADirectory=r"C:/Users/Nacho/Desktop/Repositorios/PythonScripts/SourceFiles/UnnormalizedInputFileA.csv"
    normalizedFilaADirectory=r"C:/Users/Nacho/Desktop/Repositorios/PythonScripts/SourceFiles/NormalizedInputFileA.txt"
    sortedFileADirectory=r"C:/Users/Nacho/Desktop/Repositorios/PythonScripts/SourceFiles/SortedFileA.txt"
    getSortedFileA(normalizedFilaADirectory,sortedFileADirectory)
    #normalizeInputFileA(unnormalizedFileADirectory,normalizedFilaADirectory)

    unnormalizedFileBDirectory=r"C:/Users/Nacho/Desktop/Repositorios/PythonScripts/SourceFiles/UnnormalizedInputFileB.csv"
    normalizedFileBDirectory=r"C:/Users/Nacho/Desktop/Repositorios/PythonScripts/SourceFiles/NormalizedInputFileB.txt"
    #normalizeInputFileB(unnormalizedFileBDirectory,normalizedFileBDirectory)

    differenceFileDirectory=r"C:/Users/Nacho/Desktop/Repositorios/PythonScripts/SourceFiles/differenceFile.txt"
    getDifference(sortedFileADirectory,normalizedFileBDirectory,differenceFileDirectory)
    getSortedFileA(differenceFileDirectory,r"C:/Users/Nacho/Desktop/Repositorios/PythonScripts/SourceFiles/differenceFileSorted.txt")
    
if __name__=="__main__":
    __main__()