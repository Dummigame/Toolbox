
import os

directory = os.path.dirname(os.path.realpath(__file__))
directory += '/'
print("Enter the filename of your input (it should be in the same folder or a subfolder of where you have stored this script)")

inputPath = input()

inputPath.strip()
if inputPath[0]=='.':
    inputPath=inputPath.strip(".")
if inputPath[0]=='/':
    inputPath=inputPath.strip("/")

directory += inputPath

with open(directory, "rt") as inputFile:
    print("Your input: ",inputFile.read())
    print("Which substring do you want to replace?")
    toBeReplaced = input()
    print("What do you wish to replace it with?")
    replaceWith = input()
    with open(directory, "rt") as inputFile:
        inputAsString = inputFile.read()
        inputFile.close()

directory = os.path.dirname(os.path.realpath(__file__))
directory+="/output.txt"

outputFile = open(directory, "wt")

inputAsString=inputAsString.replace(toBeReplaced, replaceWith)
outputFile.write(inputAsString)
    
print("Output: ",inputAsString, "\nSaved to", directory)
outputFile.close()
