import tkinter as tk
import os
from PIL import ImageTk, Image
from urllib.request import urlopen

## Phasmophobia Ghost helper tool.
## Made by (DeathTech) - www.twitch.tv/deathtech154
## All rights reserved.

## If you are reading this python code.
## You are welcome to read it, I have made it as readable as possible.
## Please do not copy any of the code for your own usage in part or full.
## Please do not make any derrived software for public release.

## You are welcome to tweak parts of the software but not if you are going to display those publicly
## as I do not want people thinking the tool is buggy because you can't program.

## If you have any edits you want to add officially:
## please go to the github and post a fork or suggest an edit and I will make sure it is sound..

## Do not edit the software to remove the watermark at the top.
## Do not redistribute unless express permission is given.

## You are welcome to use this software royalty free in youtube videos, streaming,...
## Although if you are going to display this software publically. Again do not remove the watermark.
## If you are a content creator using this tool you must display it on screen to avoid confusion.

## This list is not exhaustive again all rights reserved.

ToolVersion = "v1.1.1.6"

def GetLatestVersion():
    url = "https://github.com/DeathTech154/PhasmophobiaGhostHelper/wiki/Version---Changelog"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    VersionIndex = html.find("Latest Tool Version: ")
    StartLoc = VersionIndex+len("Latest Tool Version: ")
    Length = len("v0.0.0.0")
    LatestVersion = html[StartLoc:StartLoc+Length]
    return LatestVersion

WaterMark = "Made by twitch.tv/DeathTech154 | Twitter: @deathtech154 | yt: DeathTechDB"

class Ghost:
    def __init__(self,name,evidence):
        self.name = name
        self.evidence = evidence

class GhostGUI:
    def __init__(self,name,evidence,label):
        self.name = name
        self.evidence = evidence
        self.label = label
evidences = []
excludes = []
ghosts = []
ghostsGUI = []
ghosts.append(Ghost("Banshee",["Fingerprints","Orbs","DOTS"]))
ghosts.append(Ghost("Demon",["Fingerprints","Writing","Freezing"]))
ghosts.append(Ghost("Hantu",["Fingerprints","Orbs","Freezing"]))
ghosts.append(Ghost("Jinn",["EMF","Fingerprints","Freezing"]))
ghosts.append(Ghost("Mare",["Box","Orbs","Writing"]))
ghosts.append(Ghost("Oni",["EMF","Freezing","DOTS"]))
ghosts.append(Ghost("Phantom",["Box","Fingerprints","DOTS"]))
ghosts.append(Ghost("Poltergeist",["Box","Fingerprints","Writing"]))
ghosts.append(Ghost("Revenant",["Orbs","Writing","Freezing"]))
ghosts.append(Ghost("Shade",["EMF","Writing","Freezing"]))
ghosts.append(Ghost("Spirit",["EMF","Box","Writing"]))
ghosts.append(Ghost("Wraith",["EMF","Box","DOTS"]))
ghosts.append(Ghost("Yokai",["Box","Orbs","DOTS"]))
ghosts.append(Ghost("Yurei",["Orbs","Freezing","DOTS"]))
ghosts.append(Ghost("Goryo",["EMF","Fingerprints","DOTS"]))
ghosts.append(Ghost("Myling",["EMF","Fingerprints","Writing"]))

#Statistics (100 / max ghosts * evidences) = Percentage remaining
# Freezing     7 / 16, 43.75% -> Focus - Highly Reliable
# EMF          7 / 16, 43.75% -> Unreliable - Don't Bother? XD
# Orbs         6 / 16, 50.00% -> Set and monitor
# Box          6 / 16, 37.50% -> Focus - Highly Reliable
# Writing      7 / 16, 43.75% -> Set and forget - Unreliable
# Fingerprints 8 / 16, 50.00% -> Focus - Highly Reliable
# DOTS         7 / 16, 43.75% -> Reliable granted small room.

# EMF can exclude Orbs and vice versa
# BOX can exclude Freezing
# BOOK can exclude D.O.T.S

def mainloop():
    print("Welcome to the main menu.")
    print("Current Evidences: " + str(evidences))
    print("Current Excludes: " + str(excludes))
    print("These are your options:")
    print("<Add> evidence.     - Add a confirmed evidence.")
    print("<Remove> evidence.  - Remove a mistake evidence.")
    print("<Include> evidence. - Include a previously excluded evidence.")
    print("<Exclude> evidence. - Exclude an evidence if you have tried to get it.")
    print("<Show> possible ghost types. ")
    menu_action = input("> ")
    if menu_action.lower() in ["add", "ad"]:
        print("Please type evidence you wish to add or leave blank to return.")
        print("Freezing, EMF, Orbs, Box, Writing, Fingerprints")
        add = input("> Add > ")
        if add == "":
            menu_action = ""
        else:
            evidences.append(add.lower())
    if menu_action.lower() in ["remove", "rem","del"]:
        print("Please type evidence you wish to remove or leave blank to return.")
        print("Freezing, EMF, Orbs, Box, Writing, Fingerprints")
        rem = input("> Rem > ")
        if rem == "":
            menu_action = ""
        else:
            try:
                evidences.remove(rem.lower())
            except:
                print("Entry was not found.")
    if menu_action.lower() in ["exclude","excl"]:
        print("Please type evidence you wish to exclude or leave blank to return.")
        print("Freezing, EMF, Orbs, Box, Writing, Fingerprints")
        excl = input("> Excl > ")
        if excl == "":
            menu_action = ""
        else:
            excludes.append(excl.lower())
    if menu_action.lower() in ["include","incl"]:
        print("Please type evidence you wish to include or leave blank to return.")
        print("Freezing, EMF, Orbs, Box, Writing, Fingerprints")
        incl = input("> Incl > ")
        if incl == "":
            menu_action = ""
        else:
            try:
                excludes.remove(incl.lower())
            except:
                print("Entry was not found.")
    if menu_action.lower() in ["show","display","disp"]:
        displaylist = []
        EvidencesFound = len(evidences)
        print("")
        print("////////////////")
        print("Debug: Ghosts>" + str(len(ghosts)))
        print("Debug: Evidence>" + str(len(evidences)))
        print("Debug: Excludes>" + str(len(excludes)))
        print("////////////////")
        print("")
        for entry in ghosts:           # For every ghost
            excluded = False
            evidence = False
            evidencecount = 0
            #print("Debug Evidences>: " + str(len(entry.evidence)))
            for evi in entry.evidence: # For every evidence on ghost
                if evi.lower() in excludes:
                    excluded = True
                if evi.lower() in evidences:
                    evidencecount = evidencecount + 1
            if excluded == False:
                if evidencecount == EvidencesFound:
                    displaylist.append(entry)
            #print("Debug Evidences> "+str(entry.name)+">: " + str(len(entry.evidence)))
        print("Ghosts possible: " + str(len(displaylist)) + " / 14")
        print("")
        print("////////////////")
        targetlen = 30
        for Entry in displaylist:
            spaces = targetlen - len(Entry.name)
            print(Entry.name + (" "*spaces) + Entry.evidence[0] + " " + Entry.evidence[1] + " " + Entry.evidence[2])
        print("////////////////")
        print("")
    mainloop()

class Evidence():
    def __init__(self,buttonF,name):
        self.State = 0
        self.buttonF = buttonF
        self.Name = name
    def Toggle(self):
        if self.State == 0: # State nothing so far. Move to evidence
            self.buttonF.configure(bg="green")
            self.buttonF.configure(fg="black")
            self.State = self.State + 1
        elif self.State == 1: # Move from evidence to suspected.
            self.buttonF.configure(bg="yellow")
            self.buttonF.configure(fg="black")
            self.State = self.State + 1
        elif self.State == 2: # Suspect this evidence is true.
            self.buttonF.configure(bg="red")
            self.buttonF.configure(fg="white")
            self.State = self.State + 1
        elif self.State == 3: # Exclude this evidence. I suspect it's not true.
            self.buttonF.configure(bg="black")
            self.State = 0
    def Exclude(self):
        self.buttonF.configure(bg="lightgrey")
        self.buttonF.configure(fg="black")
            

class GC():
    def __init__(self,wrd):
        self.list = ["Made by twitch.tv/DeathTech154 | Twitter: @deathtech154 | yt: DeathTechDB"]
        
INDEXA = " ABCDEFGHIJKLMNOPQRSTUVWXYZ.:abcdefghijklmno|pqrstuvwxyz/0123456789@"
INDEXB = "/abcdefgh|ijklmnopqrstuvwxyz: 0123456789.ABCDEFGHIJKLMNOPQRSTUVWXYZ@"
INDEXC = ".0123456789@abcdefghijklmno|pqrstuvwxyz/:ABCDEFGHIJKLMNOPQRSTUVWXYZ "
def Str2Num(stringa):
    output = []
    CurIndex = 0
    IndexList = [INDEXA,INDEXB,INDEXC]
    for Letter in stringa:
        Useable = IndexList[CurIndex]
        output.append(Useable.find(Letter))
        CurIndex = CurIndex + 1
        if CurIndex == 3:
            CurIndex = 0
    return output

def Num2Str(num):
    output = ""
    CurIndex = 0
    IndexList = [INDEXA,INDEXB,INDEXC]
    for Entry in num:
        Useable = IndexList[CurIndex]
        output = output + Useable[Entry]
        CurIndex = CurIndex + 1
        if CurIndex == 3:
            CurIndex = 0
    return output

class MainLoopGUI():
    def __init__(self):
        self.ghosts = ghostsGUI
        self.evidences = ["Freezing","EMF","Orbs","Box","Writing","Fingerprints","D.O.T.S"]
        self.EVIDENCELIST = []
    def ResolveGhosts(self):
        requiredevidencecount = 0
        requiredsusevidencecount = 0
        bannedevidence = 0
        BLOCKED = []
        for evi in self.EVIDENCELIST:
            if evi.State == 1:
                requiredevidencecount = requiredevidencecount + 1
                if evi.Name == "EMF":
                    # MAKE ORBS GRAY
                    if BLOCKED.count(evi.Name) < 1:
                        BLOCKED.append("Orbs")
                elif evi.Name == "Orbs":
                    # MAKE EMF GRAY
                    if BLOCKED.count(evi.Name) < 1:
                        BLOCKED.append("EMF")
                elif evi.Name == "Box":
                    # MAKE FREEZING GRAY
                    if BLOCKED.count(evi.Name) < 1:
                        BLOCKED.append("Freezing")
                elif evi.Name == "Freezing":
                    # MAKE BOX GRAY
                    if BLOCKED.count(evi.Name) < 1:
                        BLOCKED.append("Box")
                elif evi.Name == "Writing":
                    # MAKE D.O.T.S GRAY
                    if BLOCKED.count(evi.Name) < 1:
                        BLOCKED.append("D.O.T.S")
                elif evi.Name == "D.O.T.S":
                    # MAKE BOOK GRAY
                    if BLOCKED.count(evi.Name) < 1:
                        BLOCKED.append("Writing")
            elif evi.State == 2:
                requiredsusevidencecount = requiredsusevidencecount + 1
            elif evi.State == 3:
                bannedevidence = bannedevidence + 1
        # GO THROUGH EVIDENCE
        # CONFIRM IF CONTRADICTIONS ARE IN PLAY
        # CONFIRM WHICH CONTRADICTIONS
        # RUN THROUGH AND GREY CONTRADICTIONS
        # RUN THROUGH AND GREY GHOST AFFECTED
        for ghost in self.ghosts:
            confirmed = 0
            suspected = 0
            excluded = 0
            for evi in self.EVIDENCELIST:
                for ghostevi in ghost.evidence:
                    if evi.Name == ghostevi:
                        if evi.State == 1:   # 1 = Confirmed
                            confirmed = confirmed + 1
                        elif evi.State == 2: # 2 = Suspecting
                            suspected = suspected + 1
                        elif evi.State == 3: # 3 = Excluded
                            excluded = excluded + 1
                        for Entry in BLOCKED:
                            if ghostevi == Entry:
                                ghost.label.configure(bg="lightgray")
                                ghost.label.configure(fg="black")
                                evi.Exclude()
            if excluded >= 1:
                ghost.label.configure(bg="red")
                ghost.label.configure(fg="white")
            elif confirmed == requiredevidencecount:
                ghost.label.configure(bg="yellow")
                ghost.label.configure(fg="black")
                if suspected == requiredsusevidencecount:
                    ghost.label.configure(bg="green")
                    ghost.label.configure(fg="white")
                    if requiredsusevidencecount >= 1:
                        if suspected == requiredsusevidencecount:
                            ghost.label.configure(bg="yellow")
                            ghost.label.configure(fg="black")
                elif suspected != requiredsusevidencecount:
                    ghost.label.configure(bg="darkred")
                    ghost.label.configure(fg="white")
            else:
                ghost.label.configure(bg="darkred")
                ghost.label.configure(fg="white")
        for evi in self.EVIDENCELIST:
            if evi.buttonF.cget("bg") == "lightgrey":
                if not evi.Name in BLOCKED:
                    evi.buttonF.configure(bg="black")
                    evi.buttonF.configure(fg="white")
        if requiredevidencecount == 0:
            if requiredsusevidencecount == 0:
                if bannedevidence == 0:
                    for ghost in self.ghosts:
                        ghost.label.configure(bg="black")

def ButtonClicked(data):
    for Entry in Game.EVIDENCELIST:
        if Entry.Name == data:
            Entry.Toggle()
    Game.ResolveGhosts()

LabelBGColor = "black"
LabelFGColor = "white"
ButtonBGOff = "black"
ButtonBGOn = "green"
ButtonTextColorOn = "black"
ButtonTextColorOff = "white"
LabelGhostPossibleBG = "black"
LabelGhostPossibleT = "white"
LabelGhostPlausibleBG = "darkyellow"
LabelGhostPlausibleT = "black"
LabelGhostExcludedBG = "red"
LabelGhostExcludedT = "white"
GhostLabelWidth = 12
GhostLabelHeight = 1

window = tk.Tk()
window.attributes('-topmost',True)
window.wm_title("Phasmophobia Ghost Helper "+ToolVersion+" - by twitch.tv/DeathTech154")
ico = Image.open('Phasmo.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)
WM = True
if WM == False:
    #window.geometry("630x100")
    pass
else:
    #window.geometry("630x120")
    wm = tk.Label(bg="black",fg="white",text=Num2Str([13, 1, 15, 33, 29, 13, 54, 29, 32, 52, 10, 32, 31, 8, 0, 49, 23, 39, 4, 5, 12, 49, 8, 60, 33, 3, 19, 58, 35, 5, 0, 9, 67, 20, 24, 20, 49, 21, 16, 47, 28, 67, 67, 4, 16, 29, 21, 19, 49, 5, 14, 36, 31, 6, 61, 29, 27, 0, 26, 32, 28, 29, 44, 33, 1, 32, 36, 60, 16, 31, 8, 44, 2]))
    wm.pack(fill=tk.BOTH, expand=True)

def HideUpdate():
    ud.destroy()

try:
    LatestVersion = GetLatestVersion()
except:
    ud = tk.Button(bg="yellow",fg="black",text="It would appear you have no internet. Can't check for updates like this. Click to supress notice for now.",command=HideUpdate)
    ud.pack(fill=tk.BOTH, expand=True)

if ToolVersion != LatestVersion:
    print("Version Comparison: " + str(ToolVersion) + " : " + LatestVersion)
    ud = tk.Button(bg="yellow",fg="black",text="Your version " + str(ToolVersion) + " is out of date (Newest: "+LatestVersion+"). Click to supress notice for now.",command=HideUpdate)
    ud.pack(fill=tk.BOTH, expand=True)

frameevidences = tk.Frame()
frameevidences.pack(fill=tk.BOTH, expand=True)

buttonwidth = 11
evidencelabel = tk.Label(master=frameevidences,text="Green:     Confirmed\nYellow:    Suspected\nRed:           Excluded",width=15,height=2,bg=LabelBGColor,fg=LabelFGColor)
buttoneviemf = tk.Button(master=frameevidences,command=lambda: ButtonClicked("EMF"),text="EMF",width=buttonwidth,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
buttoneviorbs = tk.Button(master=frameevidences,command=lambda: ButtonClicked("Orbs"),text="Orbs",width=buttonwidth,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
buttoneviwriting = tk.Button(master=frameevidences,command=lambda: ButtonClicked("Writing"),text="Writing",width=buttonwidth,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
buttonevibox = tk.Button(master=frameevidences,command=lambda: ButtonClicked("Box"),text="Spirit Box",width=buttonwidth,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
buttonevifinger = tk.Button(master=frameevidences,command=lambda: ButtonClicked("Fingerprints"),text="Fingerprints",width=buttonwidth,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
buttonevifreeze = tk.Button(master=frameevidences,command=lambda: ButtonClicked("Freezing"),text="Freezing",width=buttonwidth,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
buttonevidots = tk.Button(master=frameevidences,command=lambda: ButtonClicked("D.O.T.S"),text="D.O.T.S",width=buttonwidth,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)

Game = MainLoopGUI()
emf = Evidence(buttoneviemf,"EMF")
orbs = Evidence(buttoneviorbs,"Orbs")
writing = Evidence(buttoneviwriting,"Writing")
box = Evidence(buttonevibox,"Box")
finger = Evidence(buttonevifinger,"Fingerprints")
freeze = Evidence(buttonevifreeze,"Freezing")
dots = Evidence(buttonevidots,"D.O.T.S")
Game.EVIDENCELIST.append(emf)
Game.EVIDENCELIST.append(orbs)
Game.EVIDENCELIST.append(writing)
Game.EVIDENCELIST.append(box)
Game.EVIDENCELIST.append(finger)
Game.EVIDENCELIST.append(freeze)
Game.EVIDENCELIST.append(dots)

evidencelabel.pack(fill=tk.BOTH,side=tk.LEFT)
buttoneviemf.pack(fill=tk.BOTH,side=tk.LEFT)
buttonevibox.pack(fill=tk.BOTH,side=tk.LEFT)
buttonevifinger.pack(fill=tk.BOTH,side=tk.LEFT)
buttoneviorbs.pack(fill=tk.BOTH,side=tk.LEFT)
buttoneviwriting.pack(fill=tk.BOTH,side=tk.LEFT)
buttonevifreeze.pack(fill=tk.BOTH,side=tk.LEFT)
buttonevidots.pack(fill=tk.BOTH,side=tk.LEFT)

frameghostsa = tk.Frame()
frameghostsa.pack(fill=tk.BOTH, expand=True)

frameghostsb = tk.Frame()
frameghostsb.pack(fill=tk.BOTH, expand=True)

def show_tooltip(text):
    if text == "Banshee":
        labelban.configure(text="UV ORB DOTS") # ["Fingerprints","Orbs","DOTS"]
    elif text == "Demon":
        labeldem.configure(text="UV BOOK COLD") # ["Fingerprints","Writing","Freezing"]
    elif text == "Hantu":
        labelhan.configure(text="UV ORB COLD") # ["Fingerprints","Orbs","Freezing"]
    elif text == "Jinn":
        labeljin.configure(text="EMF UV COLD") # ["EMF","Fingerprints","Freezing"]
    elif text == "Mare":
        labelmar.configure(text="BOX ORB BOOK") # ["Box","Orbs","Writing"]
    elif text == "Oni":
        labeloni.configure(text="EMF COLD DOTS") # ["EMF","Freezing","DOTS"]
    elif text == "Phantom":
        labelpha.configure(text="BOX UV DOTS") # ["Box","Fingerprints","DOTS"]
    elif text == "Poltergeist":
        labelpol.configure(text="BOX UV BOOK") # ["Box","Fingerprints","Writing"]
    elif text == "Revenant":
        labelrev.configure(text="ORB BOOK COLD") # ["Orbs","Writing","Freezing"]
    elif text == "Shade":
        labelsha.configure(text="EMF BOOK COLD") # ["EMF","Writing","Freezing"]
    elif text == "Spirit":
        labelspi.configure(text="EMF BOX BOOK") # ["EMF","Box","Ghost Writing"]
    elif text == "Wraith":
        labelwra.configure(text="EMF BOX DOTS") # ["EMF","Box","DOTS"]
    elif text == "Yokai":
        labelyok.configure(text="BOX ORB DOTS") # ["Box","Orbs","DOTS"]
    elif text == "Yurei":
        labelyur.configure(text="ORB COLD DOTS") # ["Orbs","Freezing","DOTS"]
    elif text == "Goryo":
        labelgor.configure(text="EMF UV DOTS") # ["EMF","Fingerprints","DOTS"]
    elif text == "Myling":
        labelmyl.configure(text="EMF UV BOOK") # ["EMF","Fingerprints","Ghost Writing"]

def hide_tooltip(data):
    if data == "Banshee":
        labelban.configure(text=data)
    elif data == "Demon":
        labeldem.configure(text=data)
    elif data == "Hantu":
        labelhan.configure(text=data)
    elif data == "Jinn":
        labeljin.configure(text=data)
    elif data == "Mare":
        labelmar.configure(text=data)
    elif data == "Oni":
        labeloni.configure(text=data)
    elif data == "Phantom":
        labelpha.configure(text=data)
    elif data == "Poltergeist":
        labelpol.configure(text=data)
    elif data == "Revenant":
        labelrev.configure(text=data)
    elif data == "Shade":
        labelsha.configure(text=data)
    elif data == "Spirit":
        labelspi.configure(text=data)
    elif data == "Wraith":
        labelwra.configure(text=data)
    elif data == "Yokai":
        labelyok.configure(text=data)
    elif data == "Yurei":
        labelyur.configure(text=data)
    elif data == "Goryo":
        labelgor.configure(text=data)
    elif data == "Myling":
        labelmyl.configure(text=data)

labelban = tk.Label(master=frameghostsa,text="Banshee",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labelban.bind("<Enter>", lambda data="Banshee": show_tooltip("Banshee"))
labelban.bind("<Leave>", lambda data="Banshee": hide_tooltip("Banshee"))
labeldem = tk.Label(master=frameghostsa,text="Demon",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labeldem.bind("<Enter>", lambda data="Demon": show_tooltip("Demon"))
labeldem.bind("<Leave>", lambda data="Demon": hide_tooltip("Demon"))
labelhan = tk.Label(master=frameghostsa,text="Hantu",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labelhan.bind("<Enter>", lambda data="Hantu": show_tooltip("Hantu"))
labelhan.bind("<Leave>", lambda data="Hantu": hide_tooltip("Hantu"))
labeljin = tk.Label(master=frameghostsa,text="Jinn",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labeljin.bind("<Enter>", lambda data="Jinn": show_tooltip("Jinn"))
labeljin.bind("<Leave>", lambda data="Jinn": hide_tooltip("Jinn"))
labelmar = tk.Label(master=frameghostsa,text="Mare",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labelmar.bind("<Enter>", lambda data="Mare": show_tooltip("Mare"))
labelmar.bind("<Leave>", lambda data="Mare": hide_tooltip("Mare"))
labeloni = tk.Label(master=frameghostsa,text="Oni",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labeloni.bind("<Enter>", lambda data="Oni": show_tooltip("Oni"))
labeloni.bind("<Leave>", lambda data="Oni": hide_tooltip("Oni"))
labelpha = tk.Label(master=frameghostsa,text="Phantom",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labelpha.bind("<Enter>", lambda data="Phantom": show_tooltip("Phantom"))
labelpha.bind("<Leave>", lambda data="Phantom": hide_tooltip("Phantom"))
labelpol = tk.Label(master=frameghostsb,text="Poltergeist",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labelpol.bind("<Enter>", lambda data="Poltergeist": show_tooltip("Poltergeist"))
labelpol.bind("<Leave>", lambda data="Poltergeist": hide_tooltip("Poltergeist"))
labelrev = tk.Label(master=frameghostsb,text="Revenant",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labelrev.bind("<Enter>", lambda data="Revenant": show_tooltip("Revenant"))
labelrev.bind("<Leave>", lambda data="Revenant": hide_tooltip("Revenant"))
labelsha = tk.Label(master=frameghostsb,text="Shade",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labelsha.bind("<Enter>", lambda data="Shade": show_tooltip("Shade"))
labelsha.bind("<Leave>", lambda data="Shade": hide_tooltip("Shade"))
labelspi = tk.Label(master=frameghostsb,text="Spirit",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labelspi.bind("<Enter>", lambda data="Spirit": show_tooltip("Spirit"))
labelspi.bind("<Leave>", lambda data="Spirit": hide_tooltip("Spirit"))
labelwra = tk.Label(master=frameghostsb,text="Wraith",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labelwra.bind("<Enter>", lambda data="Wraith": show_tooltip("Wraith"))
labelwra.bind("<Leave>", lambda data="Wraith": hide_tooltip("Wraith"))
labelyok = tk.Label(master=frameghostsb,text="Yokai",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labelyok.bind("<Enter>", lambda data="Yokai": show_tooltip("Yokai"))
labelyok.bind("<Leave>", lambda data="Yokai": hide_tooltip("Yokai"))
labelyur = tk.Label(master=frameghostsb,text="Yurei",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labelyur.bind("<Enter>", lambda data="Yurei": show_tooltip("Yurei"))
labelyur.bind("<Leave>", lambda data="Yurei": hide_tooltip("Yurei"))
labelgor = tk.Label(master=frameghostsa,text="Goryo",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labelgor.bind("<Enter>", lambda data="Goryo": show_tooltip("Goryo"))
labelgor.bind("<Leave>", lambda data="Goryo": hide_tooltip("Goryo"))
labelmyl = tk.Label(master=frameghostsb,text="Myling",width=GhostLabelWidth,height=GhostLabelHeight,bg=LabelGhostPossibleBG,fg=LabelGhostPossibleT)
labelmyl.bind("<Enter>", lambda data="Myling": show_tooltip("Myling"))
labelmyl.bind("<Leave>", lambda data="Myling": hide_tooltip("Myling"))

ghostsGUI.append(GhostGUI("Banshee",["Fingerprints","Orbs","D.O.T.S"],labelban))
ghostsGUI.append(GhostGUI("Demon",["Fingerprints","Writing","Freezing"],labeldem))
ghostsGUI.append(GhostGUI("Hantu",["Fingerprints","Orbs","Freezing"],labelhan))
ghostsGUI.append(GhostGUI("Jinn",["EMF","Fingerprints","Freezing"],labeljin))
ghostsGUI.append(GhostGUI("Mare",["Box","Orbs","Writing"],labelmar))
ghostsGUI.append(GhostGUI("Oni",["EMF","Freezing","D.O.T.S"],labeloni))
ghostsGUI.append(GhostGUI("Phantom",["Box","Fingerprints","D.O.T.S"],labelpha))
ghostsGUI.append(GhostGUI("Poltergeist",["Box","Fingerprints","Writing"],labelpol))
ghostsGUI.append(GhostGUI("Revenant",["Orbs","Writing","Freezing"],labelrev))
ghostsGUI.append(GhostGUI("Shade",["EMF","Writing","Freezing"],labelsha))
ghostsGUI.append(GhostGUI("Spirit",["EMF","Box","Writing"],labelspi))
ghostsGUI.append(GhostGUI("Wraith",["EMF","Box","D.O.T.S"],labelwra))
ghostsGUI.append(GhostGUI("Yokai",["Box","Orbs","D.O.T.S"],labelyok))
ghostsGUI.append(GhostGUI("Yurei",["Orbs","Freezing","D.O.T.S"],labelyur))
ghostsGUI.append(GhostGUI("Goryo",["EMF","Fingerprints","D.O.T.S"],labelgor))
ghostsGUI.append(GhostGUI("Myling",["EMF","Fingerprints","Writing"],labelmyl))

labelban.pack(fill=tk.BOTH,side=tk.LEFT)
labeldem.pack(fill=tk.BOTH,side=tk.LEFT)
labelhan.pack(fill=tk.BOTH,side=tk.LEFT)
labeljin.pack(fill=tk.BOTH,side=tk.LEFT)
labelmar.pack(fill=tk.BOTH,side=tk.LEFT)
labeloni.pack(fill=tk.BOTH,side=tk.LEFT)
labelpha.pack(fill=tk.BOTH,side=tk.LEFT)
labelpol.pack(fill=tk.BOTH,side=tk.LEFT)
labelrev.pack(fill=tk.BOTH,side=tk.LEFT)
labelsha.pack(fill=tk.BOTH,side=tk.LEFT)
labelspi.pack(fill=tk.BOTH,side=tk.LEFT)
labelwra.pack(fill=tk.BOTH,side=tk.LEFT)
labelyok.pack(fill=tk.BOTH,side=tk.LEFT)
labelyur.pack(fill=tk.BOTH,side=tk.LEFT)
labelgor.pack(fill=tk.BOTH,side=tk.LEFT)
labelmyl.pack(fill=tk.BOTH,side=tk.LEFT)

nameinput = tk.Entry()
nameinput.configure(text="Put Ghost Name Here or drag the bottom up to hide name slot.")
nameinput.insert(0,"Put Ghost Name Here or drag the bottom up to hide name slot.")
nameinput.pack(fill=tk.BOTH, expand=True)

window.mainloop()
