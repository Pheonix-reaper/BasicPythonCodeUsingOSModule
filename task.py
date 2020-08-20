import os

print("////////////////////////                    Welcome,How may I assist you?      //////////////////////////////")
print()
while True:   
    print("- - - - - - - - - - - - - - - - - - - - - - - - -Any program you would like to run??----------------------------- ")
    n = input()
    if((("run" in n) or ("execute" in n)) and (("browser" in n) or ("explorer" in n))):
        print("Opening a Browser!")
        os.system("chrome")
    elif((("run" in n) or ("execute" in n)) and (("mediaplayer" in n) or ("wmp" in n) or ("song" in n))):
        print("Opening Windows media Player")
        os.system("wmp")
    elif((("run" in n) or ("execute" in n)) and (("notepad" in n)or("editor" in n))):
        print("Opening Text Editor")
        os.system("notepad")
    elif(("clone" in n) and ("repository" in n)):
        ID=input("Enter the github repository URL:")
        k="git clone "+ID
        os.system(k)
    elif("calculator" in n):
        print("Opening Calculator")
        os.system("calc")    
    elif(("run" in n) and (("jupyter" in n)or("IDE" in n))):
        print("Opening Jupyter IDE")
        os.system("jupyter notebook")
    elif(("run" in n) and (("paint" in n) or ("drawing software" in n))):
        print("Opening Paint Software!")
        os.system("mspaint")
    elif(("run" in n) and ("gitbash" in n)):
        print("Opening Git Bash")
        os.system("git bash")
    elif(("open" in n)and("folder" in n)):
        ID=input("Enter the IP you want to open:")
        k="curl "+ID
        os.system(k) 
    elif(("List" in n) and ("files" in n)):
        os.system("dir")                  
    elif("exit" in n):
        print("We are closing the program!")
        print("________________________________________________________________________________________________________________________")
        os.system(exit())
        break