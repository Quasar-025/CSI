import termcolor

def validity(command):
    # It checks if command string has grep as starting word.
    if(command[0:4] == "grep"):
        return True
    
def pattern(command):
    # This will split the input command and get the 2nd last
    # element of the string.
    commands_list = command.split()
    cpattern = commands_list[len(commands_list)-2]
    return cpattern

def flags(command):
    # This will remove any other inputs after and return the
    # remaining list as flags list
    commands_list = command.split()
    commands_list.pop(0)
    commands_list.pop(len(commands_list)-1)
    commands_list.pop(len(commands_list)-1)
    return commands_list

def path(command):
    # Gets the last element after splitting as path.
    commands_list = command.split()
    return commands_list[len(commands_list)-1]

def printing(content,i,f,lineNo):
    # Prints stuff.
    print(f"{lineNo+1}. ",end = "")
    for j in range(len(content)):
        if(j>=i and j<f):
            print(termcolor.colored(content[j],'yellow'),end = "")
        else:
            print(content[j],end = "")
    print()

def search(cpattern, path, flags):
    if("-c" in flags):
        case_sensitive_search(cpattern,path,tuple(flags))
    # else:
    #   case_insensitive_search(cpattern,path,tuple(flags))
    # ran out of time :((


def case_sensitive_search(cpattern, path,options):
    # Based on arguments it gets, it will search for pattern with case senstivity
    # Options: 
    #   -w gives word matches only
    #   -n gives count of the matches
    #   -i gives the lines that don't have the requested pattern

    with open(path,'r') as file:
        lines = file.readlines()

    print(termcolor.colored("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",'green'))
    print(termcolor.colored(f"Searching in file: {path}\n",'green'))
    print(termcolor.colored("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",'green'))
    resultsFound=0
    for line in lines:
        initialPos = line.find(cpattern)
        
        if(initialPos>=0 and "-i" not in options):
            finalPos = initialPos+len(cpattern)
            if("-w" in options):
                if((line[initialPos-1]==" " or initialPos==0) and (line[finalPos]==" " or line[finalPos]==".")):
                    if("-n" in options): resultsFound+=1
                    else: printing(line,initialPos,finalPos,lines.index(line))
            else:
                if("-n" in options): resultsFound+=1
                else: printing(line,initialPos,finalPos,lines.index(line))
                
        elif("-i" in options):
            if("-n" in options):
                resultsFound+=1
            else:
                printing(line,-1,-1,lines.index(line))
                
    if("-n" in options):print(f"{resultsFound} matches found.")


##################################################################################################
check = False

while(check != True):

    command = input(": ")

    if(validity(command) == True):
        cpattern = pattern(command)
        flag = flags(command)
        destination_path = path(command)
        try:
            search(cpattern,destination_path,flag)

        except IsADirectoryError:
            print("Provide path to a file")

        except FileNotFoundError:
            if('*' in destination_path):
                print("Provide file name instead of wildcard(*)")
            else:
                print("File not Found")

    elif(command == "exit"):
        check = True

    else:
        print("Command not valid!")