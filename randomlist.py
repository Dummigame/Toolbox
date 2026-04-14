import random
import os
print("How many random numbers do you wish to get?")
randomCount=input().strip()
if(randomCount==''):
    print("Default: 1")
    randomCount='1'
randomCount=int(randomCount)

print("Which type of number do you want? Integer or Decimal.")
format=input()
format.lower()
format.strip()
if(format==''):
    print("Default: decimal")

def querySeparation() -> separation:
    confirmation=False
    while confirmation==False:
        print("Type of separation?")
        separation=input()
        separation.lower()
        separation.strip()
        if(separation==''):
            print("Default: ,")
            separation=','
        if(len(separation) > 1):
            print("Multiple characters given for separation. Do you want this?")
            confirmation = input()
            if(confirmation=="yes" or confirmation=='y' or confirmation=="true" or confirmation=='1'):
                confirmation=True
            else: confirmation=False
        else: confirmation=True
    return separation

if randomCount>1: separation=querySeparation()

if(randomCount<1000):
    print("Write to file?")
    writeToFile=input()
    writeToFile.strip()
    if(writeToFile==''): print("Default: Write to stdout")
else: writeToFile='y'

if writeToFile=="yes" or writeToFile=='y' or writeToFile=="true" or writeToFile=='1':
    directory = os.path.dirname(os.path.realpath(__file__))
    directory+="/outputRandomList.txt"
    outputFile=open(directory, "wt")
    for i in range(randomCount):
        if format=="integer" or format=="int" or format=="i":
            outputFile.write(str(random.randint(0,10000)))
        else: outputFile.write(str(random.random()))
        if i<randomCount-1:
            outputFile.write(separation)
            
    print("Saved to",directory)
else: 
    for i in range(randomCount):
        if format=="integer" or format=="int" or format=="i":
            print(random.randint(0, 10000), end="")
        else: print(random.random(), end="")
        
        if i<randomCount-1:
            print(separation, end='')
        else: print("\n", end='')