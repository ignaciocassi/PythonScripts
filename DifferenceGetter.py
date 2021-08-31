def normalizeInputFile(inputFileDirectory):
    try:
        inputFile = open(inputFileDirectory,"rt")
        inputLine = inputFile.readline()
        while inputLine:
            normalizedItemName = getItemName(inputLine)
            inputLine = inputFile.readline()
    except IOError:
        print("Error")
    finally:
        inputFile.close()

def getItemName(inputLine):
    normalizedInputLine = inputLine.rstrip("\n")
    normalizedInputLine = normalizedInputLine.replace('"',"")
    fields = normalizedInputLine.split(",")
    blankItem = lambda x : True if (x != "") else False
    fields = list(filter(blankItem, fields))
    itemName = fields[1]
    lista = itemName.split("(")
    if (len(lista)>1):
        lista = lista[0:-1]
    itemName = itemName.join(lista)
    itemName = itemName.rstrip(" ")
    itemName = itemName.replace('(',"")
    itemName = itemName.replace(')',"")
    itemName = itemName.replace('.',"")
    itemName = itemName.replace("Ã‘","N")
    print(itemName+"|")
    #print(fields[1])
    return normalizedInputLine

def __main__():
    directory=r"C:/Users/Nacho/Desktop/Repositorios/PythonScripts/SourceFiles/UnnormalizedInputFile.csv"
    normalizeInputFile(directory)
    
if __name__=="__main__":
    __main__()