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

ToolVersion = "v1.0.0.0"

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
ghosts.append(Ghost("Banshee",["Freezing","EMF","Fingerprints"]))
ghosts.append(Ghost("Demon",["Freezing","Box","Writing"]))
ghosts.append(Ghost("Hantu",["Orbs","Writing","Fingerprints"]))
ghosts.append(Ghost("Jinn",["EMF","Orbs","Box"]))
ghosts.append(Ghost("Mare",["Freezing","Orbs","Box"]))
ghosts.append(Ghost("Oni",["EMF","Box","Writing"]))
ghosts.append(Ghost("Phantom",["Freezing","EMF","Orbs"]))
ghosts.append(Ghost("Poltergeist",["Orbs","Box","Fingerprints"]))
ghosts.append(Ghost("Revenant",["EMF","Writing","Fingerprints"]))
ghosts.append(Ghost("Shade",["EMF","Orbs","Writing"]))
ghosts.append(Ghost("Spirit",["Box","Writing","Fingerprints"]))
ghosts.append(Ghost("Wraith",["Freezing","Box","Fingerprints"]))
ghosts.append(Ghost("Yokai",["Orbs","Box","Writing"]))
ghosts.append(Ghost("Yurei",["Freezing","Orbs","Writing"]))

#Statistics (100 / max ghosts * evidences) = Percentage remaining
# Freezing     6 / 14, 42.85% -> Focus
# EMF          6 / 14, 42.85% -> Focus
# Orbs         8 / 14, 57.14% -> Set and monitor
# Box          8 / 14, 57.14% -> Secondary
# Writing      8 / 14, 57.14% -> Set and forget
# Fingerprints 6 / 14, 42.85% -> Focus

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
        self.evidences = ["Freezing","EMF","Orbs","Box","Writing", "Fingerprints"]
        self.EVIDENCELIST = []
    def ResolveGhosts(self):
        requiredevidencecount = 0
        requiredsusevidencecount = 0
        bannedevidence = 0
        for evi in self.EVIDENCELIST:
            if evi.State == 1:
                requiredevidencecount = requiredevidencecount + 1
            elif evi.State == 2:
                requiredsusevidencecount = requiredsusevidencecount + 1
            elif evi.State == 3:
                bannedevidence = bannedevidence + 1
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
    window.geometry("630x100")
else:
    window.geometry("630x120")
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

evidencelabel = tk.Label(master=frameevidences,text="Green:     Confirmed\nYellow:    Suspected\nRed:           Excluded",width=15,height=2,bg=LabelBGColor,fg=LabelFGColor)
buttoneviemf = tk.Button(master=frameevidences,command=lambda: ButtonClicked("EMF"),text="EMF",width=11,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
buttoneviorbs = tk.Button(master=frameevidences,command=lambda: ButtonClicked("Orbs"),text="Orbs",width=11,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
buttoneviwriting = tk.Button(master=frameevidences,command=lambda: ButtonClicked("Writing"),text="Writing",width=11,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
buttonevibox = tk.Button(master=frameevidences,command=lambda: ButtonClicked("Box"),text="Spirit Box",width=11,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
buttonevifinger = tk.Button(master=frameevidences,command=lambda: ButtonClicked("Fingerprints"),text="Fingerprints",width=11,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
buttonevifreeze = tk.Button(master=frameevidences,command=lambda: ButtonClicked("Freezing"),text="Freezing",width=11,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)

Game = MainLoopGUI()
emf = Evidence(buttoneviemf,"EMF")
orbs = Evidence(buttoneviorbs,"Orbs")
writing = Evidence(buttoneviwriting,"Writing")
box = Evidence(buttonevibox,"Box")
finger = Evidence(buttonevifinger,"Fingerprints")
freeze = Evidence(buttonevifreeze,"Freezing")
Game.EVIDENCELIST.append(emf)
Game.EVIDENCELIST.append(orbs)
Game.EVIDENCELIST.append(writing)
Game.EVIDENCELIST.append(box)
Game.EVIDENCELIST.append(finger)
Game.EVIDENCELIST.append(freeze)

evidencelabel.pack(fill=tk.BOTH,side=tk.LEFT)
buttoneviemf.pack(fill=tk.BOTH,side=tk.LEFT)
buttoneviorbs.pack(fill=tk.BOTH,side=tk.LEFT)
buttoneviwriting.pack(fill=tk.BOTH,side=tk.LEFT)
buttonevibox.pack(fill=tk.BOTH,side=tk.LEFT)
buttonevifinger.pack(fill=tk.BOTH,side=tk.LEFT)
buttonevifreeze.pack(fill=tk.BOTH,side=tk.LEFT)



##framesusevidences = tk.Frame()
##framesusevidences.pack(fill=tk.BOTH, expand=True)
##
##evidencesuslabel = tk.Label(master=framesusevidences,text="Suspected Evidence",width=15,height=2,bg=LabelBGColor,fg=LabelFGColor)
##buttonsuseviemf = tk.Button(master=framesusevidences,text="EMF",width=10,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
##buttonsuseviorbs = tk.Button(master=framesusevidences,text="Orbs",width=10,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
##buttonsuseviwriting = tk.Button(master=framesusevidences,text="Writing",width=10,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
##buttonsusevibox = tk.Button(master=framesusevidences,text="Spirit Box",width=10,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
##buttonsusevifinger = tk.Button(master=framesusevidences,text="Fingerprints",width=10,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
##buttonsusevifreeze = tk.Button(master=framesusevidences,text="Freezing",width=10,height=2,bg=ButtonBGOff,fg=ButtonTextColorOff)
##
##evidencesuslabel.pack(fill=tk.BOTH,side=tk.LEFT)
##buttonsuseviemf.pack(fill=tk.BOTH,side=tk.LEFT)
##buttonsuseviorbs.pack(fill=tk.BOTH,side=tk.LEFT)
##buttonsuseviwriting.pack(fill=tk.BOTH,side=tk.LEFT)
##buttonsusevibox.pack(fill=tk.BOTH,side=tk.LEFT)
##buttonsusevifinger.pack(fill=tk.BOTH,side=tk.LEFT)
##buttonsusevifreeze.pack(fill=tk.BOTH,side=tk.LEFT)

frameghostsa = tk.Frame()
frameghostsa.pack(fill=tk.BOTH, expand=True)

frameghostsb = tk.Frame()
frameghostsb.pack(fill=tk.BOTH, expand=True)

def show_tooltip(text):
    if text == "Banshee":
        labelban.configure(text="COLD EMF UV")
    elif text == "Demon":
        labeldem.configure(text="COLD BOX BOOK")
    elif text == "Hantu":
        labelhan.configure(text="ORB BOOK UV")
    elif text == "Jinn":
        labeljin.configure(text="EMF ORB BOX")
    elif text == "Mare":
        labelmar.configure(text="COLD ORB BOX")
    elif text == "Oni":
        labeloni.configure(text="EMF BOX BOOK")
    elif text == "Phantom":
        labelpha.configure(text="COLD EMF ORB")
    elif text == "Poltergeist":
        labelpol.configure(text="ORB BOX UV")
    elif text == "Revenant":
        labelrev.configure(text="EMF BOOK UV")
    elif text == "Shade":
        labelsha.configure(text="EMF ORB BOOK")
    elif text == "Spirit":
        labelspi.configure(text="BOX BOOK UV")
    elif text == "Wraith":
        labelwra.configure(text="COLD BOX UV")
    elif text == "Yokai":
        labelyok.configure(text="ORB BOX BOOK")
    elif text == "Yurei":
        labelyur.configure(text="COLD ORB BOOK")

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

ghostsGUI.append(GhostGUI("Banshee",["Freezing","EMF","Fingerprints"],labelban))
ghostsGUI.append(GhostGUI("Demon",["Freezing","Box","Writing"],labeldem))
ghostsGUI.append(GhostGUI("Hantu",["Orbs","Writing","Fingerprints"],labelhan))
ghostsGUI.append(GhostGUI("Jinn",["EMF","Orbs","Box"],labeljin))
ghostsGUI.append(GhostGUI("Mare",["Freezing","Orbs","Box"],labelmar))
ghostsGUI.append(GhostGUI("Oni",["EMF","Box","Writing"],labeloni))
ghostsGUI.append(GhostGUI("Phantom",["Freezing","EMF","Orbs"],labelpha))
ghostsGUI.append(GhostGUI("Poltergeist",["Orbs","Box","Fingerprints"],labelpol))
ghostsGUI.append(GhostGUI("Revenant",["EMF","Writing","Fingerprints"],labelrev))
ghostsGUI.append(GhostGUI("Shade",["EMF","Orbs","Writing"],labelsha))
ghostsGUI.append(GhostGUI("Spirit",["Box","Writing","Fingerprints"],labelspi))
ghostsGUI.append(GhostGUI("Wraith",["Freezing","Box","Fingerprints"],labelwra))
ghostsGUI.append(GhostGUI("Yokai",["Orbs","Box","Writing"],labelyok))
ghostsGUI.append(GhostGUI("Yurei",["Freezing","Orbs","Writing"],labelyur))

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

nameinput = tk.Entry()
nameinput.configure(text="Put Ghost Name Here or drag the bottom up to hide name slot.")
nameinput.insert(0,"Put Ghost Name Here or drag the bottom up to hide name slot.")
nameinput.pack(fill=tk.BOTH, expand=True)

window.mainloop()
