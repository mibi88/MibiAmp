###################################
## MibiAmp v.0.3                 ##
## =============                 ##
## by Mibi88                     ##
## Codename : v5                 ##
## License : GNU GPL v2 or later ##
###################################

import pygame
from PIL import ImageTk

file = None

try:
    import tkinter.tix as Tix
    import tkinter as Tk
    import tkinter.messagebox as msgbox
    import tkinter.filedialog as filed
except ImportError:
    import Tix
    import Tkinter as Tk
    import tkMessageBox as msgbox
    import tkFileDialog as filed
lastpos = 0
main = Tix.Tk()
main.title("MibiAmp")
main.tk.eval('package require Tix')
print(main.tix_configure())

progress = Tix.Meter(main)
progress.pack(fill = "x")

pbar = Tk.Scale(main, from_ = 0, to = 0, orient = Tk.HORIZONTAL, showvalue = False)
pbar.set(0)
pbar.pack(fill = "x")

pygame.mixer.init()
#DEFS
def setposition():
    global file
    if file != None:
        music = pygame.mixer.Sound(file)
        lenght = round(music.get_length())
        pbar.configure(to = lenght)
        pbar.set(round(pygame.mixer.music.get_pos() / 1000))
        print(round(pygame.mixer.music.get_pos() / 1000))
def unloadsong():
    global file
    pygame.mixer.music.unload()
    progress.configure(value = 0.0)
    file = None
def loadsong():
    global file
    file = filed.askopenfilename(filetypes = [("OGG files", "*.ogg"), ("All files", "*")])
    try:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.mixer.music.pause()
        pygame.mixer.music.unpause()
        print(round(pygame.mixer.music.get_volume()) * 100)
        pygame.mixer.music.set_volume(1.0)
        progress.configure(value = round(pygame.mixer.music.get_volume()))
        music = pygame.mixer.Sound(file)
        print("length", round(music.get_length()))
    except:
        msgbox.showerror("Error", "Song can't be loaded")
def play():
    global lastpos
    pygame.mixer.music.unpause()
def pause():
    pygame.mixer.music.pause()
def restart():
    #pygame.mixer.music.rewind()
    pygame.mixer.music.play()
def soundplus():
    print(pygame.mixer.music.get_volume())
    print(pygame.mixer.music.get_volume() + 0.05)
    pygame.mixer.music.set_volume(float(pygame.mixer.music.get_volume()) + 0.05)
    progress.configure(value = round(pygame.mixer.music.get_volume() * 100)/100)
def soundminus():
    print(pygame.mixer.music.get_volume())
    print(pygame.mixer.music.get_volume() - 0.05)
    pygame.mixer.music.set_volume(float(pygame.mixer.music.get_volume() - 0.05))
    progress.configure(value = round(pygame.mixer.music.get_volume() * 100)/100)
def stop():
    pygame.mixer.music.stop()
def about():
    aboutw = Tk.Toplevel()
    aboutw.transient(main)
    aboutw.title("About MibiAmp")
    infotext = Tk.Text(aboutw)
    infotext.pack(fill = "both", expand = True)
    infotext.delete(1.0, Tk.END)
    infotext.insert(Tk.END, "MibiAmp v.0.3\n=============\nby Mibi88\nCodename : v5\nLicense : GNU GPL v2 or later")
#====

#CMDS
cmds = Tk.Frame(main)

playi = ImageTk.PhotoImage(file = "play.xbm")
pausei = ImageTk.PhotoImage(file = "pause.xbm")
restarti = ImageTk.PhotoImage(file = "restart.xbm")
stopi = ImageTk.PhotoImage(file = "stop.xbm")
loadi = ImageTk.PhotoImage(file = "load.xbm")
unloadi = ImageTk.PhotoImage(file = "unload.xbm")
volumeplusi = ImageTk.PhotoImage(file = "volumeplus.xbm")
volumeminusi = ImageTk.PhotoImage(file = "volumeminus.xbm")
refprogi = ImageTk.PhotoImage(file = "refreshprogress2.xbm")
abouti = ImageTk.PhotoImage(file = "about.xbm")

playb = Tk.Button(cmds, image = playi, command = play)
playb.pack(side = Tk.LEFT)
pauseb = Tk.Button(cmds, image = pausei, command = pause)
pauseb.pack(side = Tk.LEFT)
restartb = Tk.Button(cmds, image = restarti, command = restart)
restartb.pack(side = Tk.LEFT)
stopb = Tk.Button(cmds, image = stopi, command = stop)
stopb.pack(side = Tk.LEFT)
loadb = Tk.Button(cmds, image = loadi, command = loadsong)
loadb.pack(side = Tk.LEFT)
unloadb = Tk.Button(cmds, image = unloadi, command = unloadsong)
unloadb.pack(side = Tk.LEFT)
plusb = Tk.Button(cmds, image = volumeplusi, command = soundplus)
plusb.pack(side = Tk.LEFT)
minusb = Tk.Button(cmds, image = volumeminusi, command = soundminus)
minusb.pack(side = Tk.LEFT)
refprogb = Tk.Button(cmds, image = refprogi, command = setposition)
refprogb.pack(side = Tk.LEFT)
aboutb = Tk.Button(cmds, image = abouti, command = about)
aboutb.pack(side = Tk.LEFT)

cmds.pack(fill = "both", expand = True)
#====
#BALOONS
info1 = Tix.Balloon()
info2 = Tix.Balloon()
info3 = Tix.Balloon()
info4 = Tix.Balloon()
info5 = Tix.Balloon()
info6 = Tix.Balloon()
info7 = Tix.Balloon()
info8 = Tix.Balloon()
info9 = Tix.Balloon()
info10 = Tix.Balloon()
info11 = Tix.Balloon()
#===
info1.bind_widget(progress, msg="Volume")
info2.bind_widget(playb, msg="Play")
info3.bind_widget(pauseb, msg="Pause")
info4.bind_widget(restartb, msg="Restart")
info5.bind_widget(plusb, msg="Volume + 5")
info6.bind_widget(minusb, msg="Volume - 5")
info7.bind_widget(loadb, msg="Load")
info8.bind_widget(unloadb, msg="Unload")
info9.bind_widget(stopb, msg="Stop")
info10.bind_widget(aboutb, msg="About MibiAmp")
info11.bind_widget(refprogb, msg="Refresh the song progressbar")
#=======
main.mainloop()
