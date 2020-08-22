import os
import pyttsx3


print("/////////////////////////////////////  Welcome   /////////////////////////////////////////////")
pyttsx3.speak("Welcome  Asish ,I am your Personal Assistant")
print()
while True:   
    print("- - - - - - - - - - - - - - - - - - - - - - - - -Any program you would like to run??----------------------------- ")
    pyttsx3.speak("- - - - - - - - - - - - - - - - - - - - - - - - -What Can I Do for you?")
    n = input()
    if((("run" in n) or ("execute" in n)) and (("browser" in n) or ("explorer" in n))):
        print("Opening a Browser!")
        pyttsx3.speak("Opening a Browser!")
        os.system("start chrome")
    elif((("run" in n) or ("execute" in n)) and (("mediaplayer" in n) or ("wmp" in n) or ("song" in n))):
        print("Opening Windows media Player")
        pyttsx3.speak("Opening Windows media Player")
        os.system("start wmplayer")
    elif((("run" in n) or ("execute" in n)) and (("notepad" in n)or("editor" in n))):
        pyttsx3.speak("What will be the name of your file Sir?")
        name=input("Name of the file:")
        name="notepad "+name
        print("----------   Opening Text Editor   ------------")
        pyttsx3.speak("Sir,I am opening the file you want")
        os.system(name)
    elif(("clone" in n) and ("repository" in n)):
        pyttsx3.speak("Sir,Please give me the URL of the repository")
        ID=input("Enter the github repository URL:")
        k="git clone "+ID
        pyttsx3.speak("Please wait,Cloning the repository")
        os.system(k)
        pyttsx3.speak("Cloning Successful")
    elif(("calculator" in n) or ("CALCULATOR" in n)):
        print("Opening Calculator")
        pyttsx3.speak("Opening the Calculator")
        os.system("calc")    
    elif(("run" in n) and (("jupyter" in n)or("IDE" in n))):
        pyttsx3.speak("Sir,I am Opening the IDE")	
        print("Opening Jupyter IDE")
        os.system("jupyter notebook")
    elif(("run" in n) and (("paint" in n) or ("drawing software" in n))):
        pyttsx3.speak("Sir,I am Opening the MSPAINT software")	
        print("Opening Paint Software!")
        os.system("mspaint")
    elif(("run" in n) and ("gitbash" in n)):
        pyttsx3.speak("Sir,I am Opening Git Bash,please wait")	
        print("Opening Git Bash")
        os.system("git bash")
    elif(("open" in n)and(("website" in n) or ("webpage" in n))):
        pyttsx3.speak("Sir,can you give me the IP?")	
        ID=input("Enter the IP you want to open:")
        k="curl "+ID
        os.system(k) 
    elif(("Listen" in n)and(("playlist" in n) or ("songs" in n))):
        pyttsx3.speak("Opening a site with songs")
        pyttsx3.speak("Hope it is to your liking")	
        os.system("start chrome https://www.jiosaavn.com/") 
    elif(("open" in n)and("Youtube" in n)):
        pyttsx3.speak("Opening youtube")	
        os.system("start chrome https://www.youtube.com/") 
    elif(("List" in n) and ("files" in n)):
        pyttsx3.speak("The files Present in the directory are:")
        os.system("dir")  
    elif((("current" in n)or("present" in n))and("directory" in n)):
        curDir = os.getcwd()
        pyttsx3.speak("Sir,I am printing your current working Directory")
        print(curDir) 
    elif(("new" in n)and("directory" in n)):
        pyttsx3.speak("Sir,Can you give me the name of the new directory?")	
        newdir=input("Name of directory:")
        os.mkdir(newdir)
    elif(("remove" in n)and("directory" in n)):
        pyttsx3.speak("Sir,Can you give me the name of the directory to be removed?")	
        rdir=input("Name of directory:")
        os.rmdir(rdir)
    elif(("run" in n) and("kubernetes" in n)):
        pyttsx3.speak("Opening the Kubernetes,please wait")
        print("///////////  please wait  ////////////")      
        os.system("minikube.exe start")              
    elif("exit" in n):
        pyttsx3.speak("Thank You sir, Do call me again if you need any assistance?")
        print("We are closing the program!")
        print("________________________________________________________________________________________________________________________")
        os.system(exit())
        break
