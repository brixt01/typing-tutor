#----------------------------------------  Imports  ----------------------------------------#

#Import python libraries
import tkinter as tk
import random
import csv
from datetime import datetime
import time

#Import logins file
with open('logins.csv', newline='') as file: #Open specified file
    reader = csv.reader(file)  #Set reader up to read the specified file
    global logins #Create global variable for array of logins
    logins = list(reader) #Read file and put it in global array

#Import words file
with open('words.csv', newline='') as file:
    reader = csv.reader(file)
    global words
    words = list(reader)

#Import evaluation file
with open('evaluation.csv', newline='') as file:
    reader = csv.reader(file)
    global evaluation
    evaluation = list(reader)

#Import accuracy file
with open('accuracy.csv', newline='') as file:
    reader = csv.reader(file)
    global accuracy
    accuracy = list(reader)

#Import speed file
with open('speed.csv', newline='') as file:
    reader = csv.reader(file)
    global speeds
    speed = list(reader)

#----------------------------------------  Welcome page  ----------------------------------------#
class welcomePage(): #Create class for page

    #Set up page
    def __init__(self): #When page class is run
        self.master = tk.Tk() #Create page
        self.master.title("Welcome") #Add window title
        self.master.state('zoomed') #Make page full screen

        self.title = tk.Label(self.master, text  = "Typing speed and accuracy", font=("calibri", "25")) #Create page title
        self.title.pack() #Place page title

        #Go down a line
        self.title = tk.Label(self.master, text  = "")
        self.title.pack()

        #Button to go to login/signup page
        def loginSignUp():
            self.master.destroy()
            loginSignUpPage()
        self.loginButton = tk.Button(self.master, text = "Continue", font=("calibri", "12"), command = loginSignUp)
        self.loginButton.pack()

        #Go down a line
        self.title = tk.Label(self.master, text  = "")
        self.title.pack()

        #Button to close program
        def close():
            self.master.destroy()
            exit()
        self.button = tk.Button(self.master, text = "Close program", font=("calibri", "12"), command = close)
        self.button.pack()

#----------------------------------------  Log in / sign up page  ----------------------------------------#
class loginSignUpPage():

    #Set up page
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Login/Sign up")
        self.master.state('zoomed')

        self.title = tk.Label(self.master, text  = "Do you want to login or sign up?", font=("calibri", "25"))
        self.title.pack()

        #Button to go to login page
        def login():
            self.master.destroy()
            loginPage()
        self.loginButton = tk.Button(self.master, text = "Login", font=("calibri", "12"), command = login)

        if len(logins) == 1:
            self.loginButton.configure(state="disabled")
            self.title = tk.Label(self.master, text  = "\nThere are currently no users in the database", font=("calibri", "12"))
            self.title.pack()

        #Go down a line
        self.title = tk.Label(self.master, text  = "")
        self.title.pack()

        self.loginButton.pack()

        #Button to go to sign up page
        def signUp():
            self.master.destroy()
            signUpPage()
        self.signUpButton = tk.Button(self.master, text = "Sign up", font=("calibri", "12"), command = signUp)
        self.signUpButton.pack()

        #Go down a line
        self.title = tk.Label(self.master, text  = "")
        self.title.pack()

        #Button to go back
        def welcome(): #Make function for when a button is clicked
            self.master.destroy() #Close current window
            welcomePage() #Run class for previous page
        self.button = tk.Button(self.master, text = "Back", font=("calibri", "12"), command = welcome) #Create button, which will run "welcome" when clicked
        self.button.pack() #Place button on page

#----------------------------------------  Page for logging in  ----------------------------------------#
class loginPage():

    #Set up page
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Log in")
        self.master.state("zoomed")

        self.title = tk.Label(self.master, text  = "Login", font=("calibri", "25"))
        self.title.pack()

        self.messageText = tk.Label(self.master, text = "", font=("calibri", "12"))
        self.messageText.pack()

        self.usernameText = tk.Label(self.master, text = "Username:", font=("calibri", "12"))
        self.usernameText.pack()

        self.usernameBox = tk.Entry()
        self.usernameBox.pack()

        self.passwordText = tk.Label(self.master, text = "Password:", font=("calibri", "12"))
        self.passwordText.pack()

        self.passwordBox = tk.Entry()
        self.passwordBox.pack()

        #Command for done button
        def done():

            #Get information from text boxes
            self.loginUsername = self.usernameBox.get()
            self.loginPassword = self.passwordBox.get()

            #Check username and password match known username and password
            for i in range(1, len(logins)):
                if logins[i][0] == self.loginUsername: #Check username is correct
                    if logins[i][1] == self.loginPassword: #Check password is correct
                        global user
                        user = i

                        #Go to next page
                        self.master.destroy()
                        menuPage()

                    else:
                        self.messageText.configure(text = "Incorrect username or password")
                else:
                    self.messageText.configure(text = "Incorrect username or password")

        #Create done button
        self.button = tk.Button(self.master, text = "Done", font=("calibri", "12"), command = done)
        self.button.pack()

        #Go down a line
        self.title = tk.Label(self.master, text  = "")
        self.title.pack()

        #Button to go back
        def loginSignUp():
            self.master.destroy()
            loginSignUpPage()
        self.button = tk.Button(self.master, text = "Back", font=("calibri", "12"), command = loginSignUp)
        self.button.pack()

#----------------------------------------  Page for signing up  ----------------------------------------#
class signUpPage():

    #Set up page
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Sign up")
        self.master.state("zoomed")

        self.title = tk.Label(self.master, text  = "Sign up", font=("calibri", "25"))
        self.title.pack()

        self.messageText = tk.Label(self.master, text = "", font=("calibri", "12"))
        self.messageText.pack()

        self.usernameText = tk.Label(self.master, text = "Username:", font=("calibri", "12"))
        self.usernameText.pack()

        self.usernameBox = tk.Entry()
        self.usernameBox.pack()

        self.passwordText = tk.Label(self.master, text = "Password:", font=("calibri", "12"))
        self.passwordText.pack()

        self.passwordBox = tk.Entry()
        self.passwordBox.pack()

        #Command for done button
        def done():
            #Get information from text boxes
            self.newUsername = self.usernameBox.get()
            self.newPassword = self.passwordBox.get()

            #Check if username is new
            repeat = False
            for i in range(1, len(logins)):
                if logins[i][0] == self.newUsername:
                    repeat = True

            #Check if username/password has no spaces and is new
            if " "  not in self.newUsername:
                if " "  not in self.newPassword:
                    if self.newUsername != "" and self.newPassword != "":
                        if repeat == False:

                            #Add username/password to database of known logins
                            self.messageText.configure(text = "Successfully signed up")
                            self.usernameBox.delete(0, "end")
                            self.passwordBox.delete(0, "end")
                            logins.append([str(self.newUsername), str(self.newPassword)])
                            with open('logins.csv', 'w', newline='') as file:
                                mywriter = csv.writer(file, delimiter=',')
                                mywriter.writerows(logins)

                            #Add new user to accuracy data
                            accuracy[0].append(self.newUsername)
                            for i in range (1, len(accuracy)):
                                accuracy[i].append("0 of 0")
                            with open('accuracy.csv', 'w', newline='') as file:
                                mywriter = csv.writer(file, delimiter=',')
                                mywriter.writerows(accuracy)

                            #Add new user to speed data file
                            speed[0].append(self.newUsername)
                            for i in range (1, len(accuracy)):
                                speed[i].append("0 of 0")
                            with open('speed.csv', 'w', newline='') as file:
                                mywriter = csv.writer(file, delimiter=',')
                                mywriter.writerows(speed)

            #Give error messages
                        else:
                            self.messageText.configure(text = "Username already in use")
                    else:
                        self.messageText.configure(text = "You must enter information into all boxes")
                else:
                    self.messageText.configure(text = "Password cannot contain any spaces")
            else:
                self.messageText.configure(text = "Username cannot contain spaces")

        #Create button
        self.button = tk.Button(self.master, text = "Done", font=("calibri", "12"), command = done)
        self.button.pack()

        #Go down a line
        self.title = tk.Label(self.master, text  = "")
        self.title.pack()

        #Button to go back
        def loginSignUp():
            self.master.destroy()
            loginSignUpPage()
        self.button = tk.Button(self.master, text = "Back", font=("calibri", "12"), command = loginSignUp)
        self.button.pack()

#----------------------------------------  Main menu page  ----------------------------------------#
class menuPage():

    #Set up page
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Menu")
        self.master.state("zoomed")

        self.title = tk.Label(self.master, text  = "Main menu", font=("calibri", "25"))
        self.title.pack()

        self.title = tk.Label(self.master, text  = ("Welcome,",logins[user][0]), font=("calibri", "12"))
        self.title.pack()

        #Button for progress check
        def progressCheck():
            self.master.destroy()
            progressCheckPage()

        #Check if user is new and set buttons/text accordingly
        self.exists = False
        for i in range(1, len(evaluation)):
            if evaluation[i][1] == logins[user][0]:
                self.exists = True
        if self.exists == True:
            self.button = tk.Button(self.master, text = "Check your progress", font=("calibri", "12"), command = progressCheck)
        else:
            self.button = tk.Button(self.master, text = "Check your progress", font=("calibri", "12"), command = progressCheck, state="disabled")
            self.title = tk.Label(self.master, text  = "")
            self.title.pack()
            self.title = tk.Label(self.master, text  = 'This is your first time using this program.\n', font=("calibri", "12"))
            self.title.pack()
        self.button.pack()

        #Button to go to gamemodes page
        def gamemodes():
            self.master.destroy()
            gamemodesPage()
        self.button = tk.Button(self.master, text = "Gamemodes", font=("calibri", "12"), command = gamemodes)
        self.button.pack()

        #Button to go to password change page
        def passwordChange():
            self.master.destroy()
            passwordChangePage()
        self.button = tk.Button(self.master, text = "Change your password", font=("calibri", "12"), command = passwordChange)
        self.button.pack()

        #Go down a line
        self.title = tk.Label(self.master, text  = "")
        self.title.pack()

        #Button to log out
        def logOut():
            self.master.destroy()
            logOutPage()
        self.button = tk.Button(self.master, text = "Log out", font=("calibri", "12"), command = logOut)
        self.button.pack()

        #Check if user is new and set text accordingly
        self.exists = False
        for i in range(1, len(evaluation)):
            if evaluation[i][1] == logins[user][0]:
                self.exists = True
        if self.exists == False:
            self.title = tk.Label(self.master, text  = '\nHow to use this program:', font=("calibri", "15"))
            self.title.pack()

            self.title = tk.Label(self.master, text  = '- First, complete the evaluation game mode for your current typing abilities to be evaluated.')
            self.title.pack()

            self.title = tk.Label(self.master, text  = '- The data collected from this can be seen in the "progress check" sections.')
            self.title.pack()

            self.title = tk.Label(self.master, text  = '- This data will be used to suggest words more or less often.')
            self.title.pack()

            self.title = tk.Label(self.master, text  = '- Next, practise your typing in the "speed" and "accuracy" sections (no data will be collected, as thses are practise mdoes).')
            self.title.pack()

            self.title = tk.Label(self.master, text  = '- When you feel confident enough, attempt the evaluation mode again and see how you have immproved, and update your data.')
            self.title.pack()

            self.title = tk.Label(self.master, text  = '\nWarning:', font=("calibri", "15"))
            self.title.pack()

            self.title = tk.Label(self.master, text  = '- To ensure that accuracy data will be correct, the backspace key works differently.')
            self.title.pack()

            self.title = tk.Label(self.master, text  = '- If you press the backspace key once, the entire word will be cleared, and it will count as you getting the word incorrect.')
            self.title.pack()

#----------------------------------------  Progress check page  ----------------------------------------#
class progressCheckPage():

    #Set up page
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Your progress")
        self.master.state("zoomed")

        self.title = tk.Label(self.master, text  = "Your progress", font=("calibri", "25"))
        self.title.pack()

        #Button to go to evaluation check page
        def evaluationCheck():
            self.master.destroy()
            evaluationCheckPage()
        self.button = tk.Button(self.master, text = "Evaluation progress check", font=("calibri", "12"), command = evaluationCheck)
        self.button.pack()

        #Button to go to all users check page
        def allUsersCheck():
            self.master.destroy()
            allUsersCheckPage()
        self.button = tk.Button(self.master, text = "All users progress check", font=("calibri", "12"), command = allUsersCheck)
        self.button.pack()

        #Button to go to speed check page
        def speedCheck():
            self.master.destroy()
            speedCheckPage()
        self.button = tk.Button(self.master, text = "Speed progress check", font=("calibri", "12"), command = speedCheck)
        self.button.pack()

        #Button to go to accuracy check page
        def accuracyCheck():
            self.master.destroy()
            accuracyCheckPage()
        self.button = tk.Button(self.master, text = "Accuracy progress check", font=("calibri", "12"), command = accuracyCheck)
        self.button.pack()

        #Go down a line
        self.title = tk.Label(self.master, text  = "")
        self.title.pack()

        #Button to go back to menu page
        def menu():
            self.master.destroy()
            menuPage()
        self.button = tk.Button(self.master, text = "Back", font=("calibri", "12"), command = menu)
        self.button.pack()

#----------------------------------------  Evaluation check page  ----------------------------------------#
class evaluationCheckPage():

    #Set up page
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Evaluation progress check")
        self.master.state("zoomed")

        self.title = tk.Label(self.master, text  = "Evaluation progress check", font=("calibri", "25"))
        self.title.pack()

        progressList = tk.Listbox(self.master)
        progressList.pack(fill = "both")

        self.message = tk.Label(self.master, text  = "Please scroll to see the full list", font=("calibri", "12"))
        self.message.pack()

        #Add to list of previous evaluation data
        for i in range(1, len(evaluation)):
            if evaluation[i][1] == logins[user][0]:
                currentRow = str(evaluation[i][0])+" - "+str(int(evaluation[i][2]))+"% - "+str(evaluation[i][3])
                progressList.insert("end", currentRow)

        #Button to go back
        def progressCheck():
            self.master.destroy()
            progressCheckPage()
        self.button = tk.Button(self.master, text = "Back", font=("calibri", "12"), command = progressCheck)
        self.button.pack()

#----------------------------------------  All users check page  ----------------------------------------#
class allUsersCheckPage():

    #Set up page
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("All users progress check")
        self.master.state("zoomed")

        self.title = tk.Label(self.master, text  = "All users progress check", font=("calibri", "25"))
        self.title.pack()

        progressList = tk.Listbox(self.master)
        progressList.pack(fill = "both")

        self.message = tk.Label(self.master, text  = "Please scroll to see the full list", font=("calibri", "12"))
        self.message.pack()

        #Add to list of previous user data
        for i in range(1, len(evaluation)):
            currentRow = str(evaluation[i][0])+" - "+evaluation[i][1]+" - "+str(int(evaluation[i][2]))+"% - "+str(evaluation[i][3])
            progressList.insert("end", currentRow)

        #Button to go back
        def progressCheck():
            self.master.destroy()
            progressCheckPage()
        self.button = tk.Button(self.master, text = "Back", font=("calibri", "12"), command = progressCheck)
        self.button.pack()

#----------------------------------------  Speed check page  ----------------------------------------#
class speedCheckPage():

    #Set up page
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Speed progress check")
        self.master.state("zoomed")

        self.title = tk.Label(self.master, text  = "Speed progress check", font=("calibri", "25"))
        self.title.pack()

        self.progressList = tk.Listbox(self.master)
        self.progressList.pack(fill = "both")

        self.message = tk.Label(self.master, text  = "Please scroll to see the full list", font=("calibri", "12"))
        self.message.pack()

        #Create list of previous speed data
        for i in range(1, len(speed)):
            self.split = speed[i][user].split(" of ")
            if int(self.split[1]) > 0:
                self.currentRow = str(speed[i][0]) + " - " + str(round(float(self.split[0]), 2)) + "s to answer - Answered " + str(self.split[1]) + " time(s)"
            else:
                self.currentRow = str(speed[i][0]) + " - " "Never answered"
            self.progressList.insert("end", self.currentRow)

        #Button to go back
        def progressCheck():
            self.master.destroy()
            progressCheckPage()
        self.button = tk.Button(self.master, text = "Back", font=("calibri", "12"), command = progressCheck)
        self.button.pack()
        self.button.pack()

#----------------------------------------  Accuracy check page  ----------------------------------------#
class accuracyCheckPage():

    #Set up page
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Accuracy progress check")
        self.master.state("zoomed")

        self.title = tk.Label(self.master, text  = "Accuracy progress check", font=("calibri", "25"))
        self.title.pack()

        self.progressList = tk.Listbox(self.master)
        self.progressList.pack(fill = "both")

        self.message = tk.Label(self.master, text  = "Please scroll to see the full list", font=("calibri", "12"))
        self.message.pack()

        #Add to list of previous accuracy data
        for i in range(1, len(accuracy)):
            self.split = accuracy[i][user].split(" of ")
            try:
                self.percent = int(int(self.split[0]) / int(self.split[1]) * 100)
                self.currentRow = str(accuracy[i][0]) + " - " + str(accuracy[i][user] + " - " + str(self.percent) + "%")
            except:
                self.currentRow = str(accuracy[i][0]) + " - " + str(accuracy[i][user] + " - " + "Never answered")
            self.progressList.insert("end", self.currentRow)

        #Button to go back to progress check page
        def progressCheck():
            self.master.destroy()
            progressCheckPage()
        self.button = tk.Button(self.master, text = "Back", font=("calibri", "12"), command = progressCheck)
        self.button.pack()

#----------------------------------------  Gamemodes page  ----------------------------------------#
class gamemodesPage():
    #Set up page
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Gamemodes")
        self.master.state("zoomed")

        self.title = tk.Label(self.master, text  = "Gamemodes", font=("calibri", "25"))
        self.title.pack()

        #Button for evaluation gamemode
        def evaluationGamemode():
            self.master.destroy()
            evaluationPage()
        self.button = tk.Button(self.master, text = "Evaluation", font=("calibri", "12"), command = evaluationGamemode)
        self.button.pack()

        #Button for speed gamemode
        def speedGamemode():
            self.master.destroy()
            speedPage()

        #Button for accuracy gamemode
        def accuracyGamemode():
            self.master.destroy()
            accuracyPage()

        #Check if user is new and set speed/accuracy buttons accordingly
        self.exists = False
        for i in range(1, len(evaluation)):
            if evaluation[i][1] == logins[user][0]:
                self.exists = True
        if self.exists == True:
            self.speedButton = tk.Button(self.master, text = "Speed", font=("calibri", "12"), command = speedGamemode)
            self.accuracyButton = tk.Button(self.master, text = "Accuracy", font=("calibri", "12"), command = accuracyGamemode)
        else:
            self.speedButton = tk.Button(self.master, text = "Speed", font=("calibri", "12"), command = speedGamemode, state="disabled")
            self.accuracyButton = tk.Button(self.master, text = "Accuracy", font=("calibri", "12"), command = accuracyGamemode, state="disabled")
        self.speedButton.pack()
        self.accuracyButton.pack()

        #Go down a line
        self.title = tk.Label(self.master, text  = "")
        self.title.pack()

        #Button to go back to menu page
        def menu():
            self.master.destroy()
            menuPage()
        self.button = tk.Button(self.master, text = "Back", font=("calibri", "12"), command = menu)
        self.button.pack()

#----------------------------------------  Password change page  ----------------------------------------#
class passwordChangePage():

    #Set up page
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Change your password")
        self.master.state("zoomed")

        self.title = tk.Label(self.master, text  = "Change your password", font=("calibri", "25"))
        self.title.pack()

        self.newPasswordText = tk.Label(self.master, text = "New password:", font=("calibri", "12"))
        self.newPasswordText.pack()

        self.newPasswordBox = tk.Entry()
        self.newPasswordBox.pack()

        self.oldPasswordText = tk.Label(self.master, text = "Old password:", font=("calibri", "12"))
        self.oldPasswordText.pack()

        self.oldPasswordBox = tk.Entry()
        self.oldPasswordBox.pack()

        self.messageText = tk.Label(self.master, text = "", font=("calibri", "12"))
        self.messageText.pack()

        #Command for done button
        def done():
            #Get information from text boxes
            self.oldPassword = self.oldPasswordBox.get()
            self.newPassword = self.newPasswordBox.get()

            #If correct password/has no spaces/is not empty
            if logins[user][1] == self.oldPassword:
                if " "  not in self.newPassword:
                    if self.newPassword != "":

                        #Change password in known users/passwords file
                        logins[user][1] = self.newPassword
                        with open('logins.csv', 'w', newline='') as file:
                            mywriter = csv.writer(file, delimiter=',')
                            mywriter.writerows(logins)

                        #Go back to menu page
                        self.master.destroy()
                        menuPage()

            #Error messages
                    else:
                        print("no information entered in box")
                        self.messageText.configure(text = "You must enter information into all boxes")
                else:
                    print("spaces in password")
                    self.messageText.configure(text = "Password cannot contain spaces")
            else:
                print("incorrect password entered")
                self.messageText.configure(text = "Incorrect password")

        #Create button
        self.button = tk.Button(self.master, text = "Done", font=("calibri", "12"), command = done)
        self.button.pack()

        #Go down a line
        self.title = tk.Label(self.master, text  = "")
        self.title.pack()

        #Button to go back
        def menu():
            self.master.destroy()
            menuPage()
        self.button = tk.Button(self.master, text = "Back", font=("calibri", "12"), command = menu)
        self.button.pack()

#----------------------------------------  Log out page  ----------------------------------------#
class logOutPage():

    #Set up page
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Log out")
        self.master.state("zoomed")

        self.title = tk.Label(self.master, text  = "Are you sure?", font=("calibri", "25"))
        self.title.pack()

        #Button for yes
        def loginSignUp():
            self.master.destroy()
            loginSignUpPage()
        self.button = tk.Button(self.master, text = "Yes", font=("calibri", "12"), command = loginSignUp)
        self.button.pack()

        #Go down a line
        self.title = tk.Label(self.master, text  = "")
        self.title.pack()

        #Button to go back to menu page
        def menu():
            self.master.destroy()
            menuPage()
        self.button = tk.Button(self.master, text = "Back", font=("calibri", "12"), command = menu)
        self.button.pack()

#----------------------------------------  Evaluation page  ----------------------------------------#
class evaluationPage():

    #Set up page
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Evaluation")
        self.master.state("zoomed")

        #Set Up constants
        self.points = -1
        self.total = -1
        self.currentWordID = 0
        self.typeTimes = []

        self.title = tk.Label(self.master, text  = "Type the word in the text box below, then press enter to submit.", font=("calibri", "12"))
        self.title.pack()

        self.currentWord = ""
        self.currentWordText = tk.Label(self.master, text = self.currentWord, font=("calibri", "25"))
        self.currentWordText.pack()

        self.nextWord = ""
        self.nextWordText = tk.Label(self.master, text = self.nextWord, font=("calibri", "12"))
        self.nextWordText.pack()

        #Go down a line
        self.title = tk.Label(self.master, text  = "")
        self.title.pack()

        self.currentSpeed = "0 wpm"
        self.currentSpeedText = tk.Label(self.master, text = self.currentSpeed, font=("calibri", "12"))
        self.currentSpeedText.pack()

        self.master.bind("<Return>", self.enterPressed)
        self.master.bind("<BackSpace>", self.backspacePressed)

        self.textBox = tk.Entry()
        self.textBox.pack()

        self.currentWordText.configure(text = "Press enter to begin")

        #Button to go back
        def gamemodes():
            self.master.destroy()
            gamemodesPage()
        self.button = tk.Button(self.master, text = "Back (no progress will be saved)", font=("calibri", "12"), command = gamemodes)
        self.button.pack()

    #Change current word
    def newWord(self):

        #Begin timer
        self.startTime = time.time()

        #If there are more words left then change word
        if self.currentWordID < len(words)-1:
            self.currentWordID = self.currentWordID + 1
            self.currentWord = words[self.currentWordID][0]
            self.currentWordText.configure(text = self.currentWord)
            self.textBox.delete(0, "end")

            try:
                self.nextWord = words[self.currentWordID+1][0]
                self.nextWordText.configure(text = self.nextWord)
            except IndexError:
                self.nextWordText.configure(text = "")

        #If there are no more words left then save data
        else:
            self.now = datetime.now()
            self.date = self.now.strftime("%d/%m/%Y (%H:%M)")
            evaluation.append([self.date, logins[user][0], str(int((self.points / self.total)*100)), self.currentSpeed])

            #save data in accuracy/speed/evaluation files
            with open('accuracy.csv', 'w', newline='') as file:
                mywriter = csv.writer(file, delimiter=',')
                mywriter.writerows(accuracy)
            with open('speed.csv', 'w', newline='') as file:
                mywriter = csv.writer(file, delimiter=',')
                mywriter.writerows(speed)
            with open('evaluation.csv', 'w', newline='') as file:
                mywriter = csv.writer(file, delimiter=',')
                mywriter.writerows(evaluation)

            #Go to gamemodes page
            self.master.destroy()
            gamemodesPage()

    #When backspace key pressed
    def backspacePressed(self, event):
        self.answer = self.textBox.get()
        if self.answer != "":
            self.total = self.total + 1

            #Add data to database
            self.split = accuracy[self.currentWordID][user].split(" of ")
            self.split[1] = int(self.split[1])+1
            accuracy[self.currentWordID][user] = str(self.split[0]) + " of " + str(self.split[1])

        #Clear box
        self.textBox.delete(0, "end")

    #When enter key pressed
    def enterPressed(self, event):
        self.answer = self.textBox.get()
        self.endTime = time.time()

        #If answer is correct then add to score
        if self.answer == self.currentWord:
            self.total = self.total + 1
            self.points = self.points + 1

            #Time the word and calculate wpm
            try:
                self.timeToType = self.endTime - self.startTime
                self.typeTimes.append(self.timeToType - 0.2)
                self.speed = 0
                for i in range (0, len(self.typeTimes)):
                    self.speed = self.speed + self.typeTimes[i]
                self.speed = round(60 / (self.speed / len(self.typeTimes)), 3)
                self.currentSpeed = str(int(self.speed))+" wpm"
                self.currentSpeedText.configure(text = self.currentSpeed)
            except:
                pass

            #Attempt to add data to database
            try:
                self.split = accuracy[self.currentWordID][user].split(" of ")
                self.split[0] = int(self.split[0])+1
                self.split[1] = int(self.split[1])+1
                accuracy[self.currentWordID][user] = str(self.split[0]) + " of " + str(self.split[1])

                self.split = speed[self.currentWordID][user].split(" of ")
                self.split[1] = str(int(self.split[1]) + 1)
                self.split[0] = str((float(self.split[0]) + self.timeToType) / 2)
                speed[self.currentWordID][user] = str(self.split[0]) + " of " + str(self.split[1])
            except:
                pass

            #Go to next word
            self.textBox.delete(0, "end")
            self.newWord()

        #If answer is incorrect then add to score
        else:
            self.total = self.total + 1

            #Add data to database
            self.split = accuracy[self.currentWordID][user].split(" of ")
            self.split[1] = int(self.split[1])+1
            accuracy[self.currentWordID][user] = str(self.split[0]) + " of " + str(self.split[1])

            #Clear box
            self.textBox.delete(0, "end")

#----------------------------------------  Speed page  ----------------------------------------#
class speedPage():

    #Set up page
    def __init__(self):
        self.totalAnswers = 0
        self.totalSpeed = 0

        self.master = tk.Tk()
        self.master.title("Speed")
        self.master.state("zoomed")

        self.title = tk.Label(self.master, text  = "Type the word in the text box below, then press enter to submit.", font=("calibri", "12"))
        self.title.pack()

        self.currentWord = ""
        self.currentWordText = tk.Label(self.master, text = self.currentWord, font=("calibri", "25"))
        self.currentWordText.pack()

        self.currentSpeed = "Last word: 0 wpm"
        self.currentSpeedText = tk.Label(self.master, text = self.currentSpeed, font=("calibri", "12"))
        self.currentSpeedText.pack()

        self.averageSpeed = "Average speed: 0 wpm"
        self.averageSpeedText = tk.Label(self.master, text = self.averageSpeed, font=("calibri", "12"))
        self.averageSpeedText.pack()

        self.master.bind("<Return>", self.enterPressed)
        self.master.bind("<BackSpace>", self.backspacePressed)

        self.textBox = tk.Entry()
        self.textBox.pack()

        self.currentWordText.configure(text = "Press enter to begin")

        #Button to go back to gamemodes page
        def gamemodes():
            self.master.destroy()
            gamemodesPage()
        self.button = tk.Button(self.master, text = "Back", font=("calibri", "12"), command = gamemodes)
        self.button.pack()

    #Change current word
    def newWord(self):

        #Begin timer
        self.startTime = time.time()

        #Add data to database
        self.speedValues = []
        self.speedProbabilities = []
        for i in range(1, len(speed)):
            self.split = speed[i][user].split(" of ")
            self.speedValues.append(i)
            self.speedProbabilities.append((float(self.split[0])))

        #Next word
        self.currentWordID = random.choices(self.speedValues, self.speedProbabilities)[0]
        self.currentWord = words[self.currentWordID][0]
        self.currentWordText.configure(text = self.currentWord)

        #Clear box
        self.textBox.delete(0, "end")

    #When backspace key pressed, clear box
    def backspacePressed(self, event):
        self.textBox.delete(0, "end")

    #When enter key pressed
    def enterPressed(self, event):
        self.answer = self.textBox.get()
        self.endTime = time.time()

        #If answer is correct then change the word
        if self.answer == self.currentWord:
            try:
                self.timeToType = self.endTime - self.startTime
                self.currentSpeed = "Last word: " + str(int(60 / self.timeToType)) + " wpm"
                self.currentSpeedText.configure(text = self.currentSpeed)

                self.totalSpeed = self.totalSpeed + (60 / self.timeToType)
                print(self.totalSpeed)
                self.totalAnswers = self.totalAnswers + 1

                self.averageSpeed = self.totalSpeed / self.totalAnswers
                self.averageSpeedText.configure(text = "Average speed: "+ str(int(self.averageSpeed)))
            except:
                pass
            self.newWord()

        #Clear box
        self.textBox.delete(0, "end")

#----------------------------------------  Accuracy  ----------------------------------------#
class accuracyPage():

    #Set up page
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Accuracy")
        self.master.state("zoomed")

        #Set up constants
        self.points = -1
        self.total = -1

        self.title = tk.Label(self.master, text  = "Type the word in the text box below, then press enter to submit.", font=("calibri", "12"))
        self.title.pack()

        self.currentWord = ""
        self.currentWordText = tk.Label(self.master, text = self.currentWord, font=("calibri", "25"))
        self.currentWordText.pack()

        self.currentScore = "Current score: 0/0"
        self.currentScoreText = tk.Label(self.master, text = self.currentScore, font=("calibri", "12"))
        self.currentScoreText.pack()

        self.master.bind("<Return>", self.enterPressed)
        self.master.bind("<BackSpace>", self.backspacePressed)

        self.textBox = tk.Entry()
        self.textBox.pack()

        self.currentWordText.configure(text = "Press enter to begin")

        #Button to go back to gamemodes page
        def gamemodes():
            self.master.destroy()
            gamemodesPage()
        self.button = tk.Button(self.master, text = "Back", font=("calibri", "12"), command = gamemodes)
        self.button.pack()

    #Change current word
    def newWord(self):

        #Add data to databases
        self.accuracyValues = []
        self.accuracyTotal = 0
        self.accuracyProbabilities = []

        for i in range(1, len(speed)):
            self.split = speed[i][user].split(" of ")
            self.accuracyValues.append(i)
            self.accuracyTotal = self.accuracyTotal + 1/(float(self.split[0]) / float(self.split[1]))

        for i in range(1, len(accuracy)):
            self.split = accuracy[i][user].split(" of ")
            self.accuracyProbabilities.append((1/(float(self.split[0]) / float(self.split[1]))) / self.accuracyTotal)

        #New word
        self.currentWordID = random.choices(self.accuracyValues, self.accuracyProbabilities)[0]
        self.currentWord = words[self.currentWordID][0]
        self.currentWordText.configure(text = self.currentWord)

        #Clear box
        self.textBox.delete(0, "end")

    #When backspace key pressed then clear box
    def backspacePressed(self, event):
        self.total = self.total + 1
        self.currentScoreText.configure(text = ("Current score: " + str(self.points) +"/" + str(self.total)))
        self.textBox.delete(0, "end")

    #When enter key pressed
    def enterPressed(self, event):
        self.answer = self.textBox.get()

        #Add to points (and change word)
        if self.answer == self.currentWord:
            self.points = self.points + 1
            self.newWord()
        self.total = self.total + 1
        self.currentScoreText.configure(text = ("Current score: " + str(self.points) +"/" + str(self.total)))

        #Clear box
        self.textBox.delete(0, "end")

#----------------------------------------  Main  ----------------------------------------#
Main = welcomePage()
Main.master.mainloop()
