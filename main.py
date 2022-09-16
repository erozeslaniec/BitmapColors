from PIL import Image
import glob, os

oldIconsDir="/home/grafotronic/PycharmProjects/pythonProject/Icons"
newIconsDir="/home/grafotronic/PycharmProjects/pythonProject/newIcons"

os.chdir(oldIconsDir)
listOfFiles=[]
for file in glob.glob("*png"):
    listOfFiles.append(file)
print(listOfFiles)

def changeColor(oldColor, newColor, fileName, fileDir, newFileDir):
    for file in listOfFiles:
        image = Image.open(fileDir+"/"+fileName)
        image_data=image.load()
        height, width =(image.size)
        for y in range(height):
            for x in range(width):
                r,g,b,t =image_data[y,x]
                if r == oldColor[0] and g==oldColor[1] and b==oldColor[2] and t==oldColor[3]:
                    image_data[y,x] = (newColor[0], newColor[1], newColor[2], newColor[3])
        image.save(newFileDir +"/"+ fileName)

def changeEverythingExcept(exceptColor, newColor, fileName, fileDir, newFileDir):
    image = Image.open(fileDir+"/"+fileName)
    image_data=image.load()
    height, width =(image.size)
    for y in range(height):
        for x in range(width):
            r,g,b,t =image_data[y,x]
            if r != exceptColor[0] or g!=exceptColor[1] or b!=exceptColor[2] or t!=exceptColor[3]:
                image_data[y,x] = (newColor[0], newColor[1], newColor[2], newColor[3])
    image.save(newFileDir +"/"+ fileName)

def printUsedColors(fileName, fileDir):
    image = Image.open(fileDir+"/"+fileName)
    image_data=image.load()
    height, width =(image.size)
    setsOfColor = {}
    setsOfColor = set()
    for y in range(height):
        for x in range(width):
            setsOfColor.add(image_data[y,x])
    listOfColor = list(setsOfColor)
    for list2 in listOfColor:
        print(list2)

printUsedColors('logo WLE.png', oldIconsDir)
