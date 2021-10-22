
from tkinter import simpledialog
import tkinter
import persisten as p
import pygame as pg

import time
pg.mixer.init()
pg.init()

def option1():
    
    nota = p.load()
    dic = {nota[0]:"do-1",nota[1]:"re-1",nota[2]:"mi-1",nota[3]:"fa-1",nota[4]:"sol-1",nota[5]:"la-1",nota[6]:"si-1",nota[7]:"do-2",nota[8]:"re-2",nota[9]:"mi-2",nota[10]:"fa-2",nota[11]:"sol-2",nota[12]:"la-2",nota[13]:"si-2",nota[14]:"do-3",nota[15]:"re-3",nota[16]:"mi-3",nota[17]:"fa-3",nota[18]:"sol-3",nota[19]:"la-3",nota[20]:"si-3",nota[21]:"do-4"}
    frequencys = []
    List = []
    x = 0
    g = 0
    lines = []
    
    c = 0
    name = ask1()
    with open(name)as f:
        lines = f.readlines()
        
    while (c<len(lines)):
        List = []
        convert = []
        x = 0
        g = 0
        notes = lines[c]
        List = notes.split(",")
        while(g<len(List)):
            
            if(List[g] == nota[0]):
                frequencys.append('SOUNDS/c1.wav') #    C1
                convert.append(dic[nota[0]])
                g = g + 1
            elif(List[g] == nota[1]):
                frequencys.append('SOUNDS/d1.wav') #   D1
                convert.append(dic[nota[1]])
                g = g + 1
            elif(List[g] == nota[2]):
                frequencys.append('SOUNDS/e1.wav')# E1
                convert.append(dic[nota[2]])
                g = g + 1
            elif(List[g] == nota[3]):
                frequencys.append('SOUNDS/f1.wav')#F1
                convert.append(dic[nota[3]])
                g = g + 1
            elif(List[g] == nota[4]):
                frequencys.append('SOUNDS/g1.wav')#G1
                convert.append(dic[nota[4]])
                g = g + 1
            elif(List[g] == nota[5]):
                frequencys.append('SOUNDS/a1.wav')#A1
                convert.append(dic[nota[5]])
                g = g + 1
            elif(List[g] == nota[6]):
                frequencys.append('SOUNDS/b1.wav')#B1
                convert.append(dic[nota[6]])
                g = g + 1
            elif(List[g] == nota[7]):
                frequencys.append('SOUNDS/c2.wav')#    C2
                convert.append(dic[nota[7]])
                g = g + 1
            elif(List[g] == nota[8]):
                frequencys.append('SOUNDS/d2.wav')
                convert.append(dic[nota[8]])
                g = g + 1
            elif(List[g] == nota[9]):
                frequencys.append('SOUNDS/e2.wav')
                convert.append(dic[nota[9]])
                g = g + 1
            elif(List[g] == nota[10]):
                frequencys.append('SOUNDS/f2.wav')
                convert.append(dic[nota[10]])
                g = g + 1
            elif(List[g] == nota[11]):
                frequencys.append('SOUNDS/g2.wav')
                convert.append(dic[nota[11]])
                g = g + 1
            elif(List[g] == nota[12]):
                frequencys.append('SOUNDS/a2.wav')
                convert.append(dic[nota[12]])
                g = g + 1
            elif(List[g] == nota[13]):
                frequencys.append('SOUNDS/b2.wav')
                convert.append(dic[nota[13]])
                g = g + 1
            elif(List[g] == nota[14]):
                frequencys.append('SOUNDS/c3.wav')#    C3
                convert.append(dic[nota[14]])
                g = g + 1
            elif(List[g] == nota[15]):
                frequencys.append('SOUNDS/d3.wav')
                convert.append(dic[nota[15]])
                g = g + 1
            elif(List[g] == nota[16]):
                frequencys.append('SOUNDS/e3.wav')
                convert.append(dic[nota[16]])
                g = g + 1
            elif(List[g] == nota[17]):
                frequencys.append('SOUNDS/f3.wav')
                convert.append(dic[nota[17]])
                g = g + 1
            elif(List[g] == nota[18]):
                frequencys.append('SOUNDS/g3.wav')
                convert.append(dic[nota[18]])
                g = g + 1
            elif(List[g] == nota[19]):
                frequencys.append('SOUNDS/a3.wav')
                convert.append(dic[nota[19]])
                g = g + 1
            elif(List[g] == nota[20]):
                frequencys.append('SOUNDS/b3.wav')
                convert.append(dic[nota[20]])
                g = g + 1
            elif(List[g] == nota[21]):
                frequencys.append('SOUNDS/c4.wav')
                convert.append(dic[nota[21]])
                g = g + 1
            elif(List[g] == "\n"):
                g = g+1
            elif(List[g] == ''):
                g = g+1
            else:
                print(List)
                tkinter.messagebox.showinfo(title = 'result', message =  "invalid note was typed")
                break
        c = c  + 1
        string = ','.join(convert)
        tkinter.messagebox.showinfo(title = 'result', message = string)
        for x in range(len(List)-1):
            pg.mixer.Sound(frequencys[x]).play()
            time.sleep(1.5);
        print(" ") 

def option2():
    nota = p.load()
    dic = {nota[0]:"do-1",nota[1]:"re-1",nota[2]:"mi-1",nota[3]:"fa-1",nota[4]:"sol-1",nota[5]:"la-1",nota[6]:"si-1",nota[7]:"do-2",nota[8]:"re-2",nota[9]:"mi-2",nota[10]:"fa-2",nota[11]:"sol-2",nota[12]:"la-2",nota[13]:"si-2",nota[14]:"do-3",nota[15]:"re-3",nota[16]:"mi-3",nota[17]:"fa-3",nota[18]:"sol-3",nota[19]:"la-3",nota[20]:"si-3",nota[21]:"do-4"}
    frequencys = []
    List = []
    x = 0
    g = 0
    convert = []
    c = 0
    
    notes = ask2()
    List = notes.split(",")
    while(g<len(List)):
            if(List[g] == nota[0]):
                frequencys.append('SOUNDS/c1.wav') #    C1
                convert.append(dic[nota[0]])
                g = g + 1
            elif(List[g] == nota[1]):
                frequencys.append('SOUNDS/d1.wav') #   D1
                convert.append(dic[nota[1]])
                g = g + 1
            elif(List[g] == nota[2]):
                frequencys.append('SOUNDS/e1.wav')# E1
                convert.append(dic[nota[2]])
                g = g + 1
            elif(List[g] == nota[3]):
                frequencys.append('SOUNDS/f1.wav')#F1
                convert.append(dic[nota[3]])
                g = g + 1
            elif(List[g] == nota[4]):
                frequencys.append('SOUNDS/g1.wav')#G1
                convert.append(dic[nota[4]])
                g = g + 1
            elif(List[g] == nota[5]):
                frequencys.append('SOUNDS/a1.wav')#A1
                convert.append(dic[nota[5]])
                g = g + 1
            elif(List[g] == nota[6]):
                frequencys.append('SOUNDS/b1.wav')#B1
                convert.append(dic[nota[6]])
                g = g + 1
            elif(List[g] == nota[7]):
                frequencys.append('SOUNDS/c2.wav')#    C2
                convert.append(dic[nota[7]])
                g = g + 1
            elif(List[g] == nota[8]):
                frequencys.append('SOUNDS/d2.wav')
                convert.append(dic[nota[8]])
                g = g + 1
            elif(List[g] == nota[9]):
                frequencys.append('SOUNDS/e2.wav')
                convert.append(dic[nota[9]])
                g = g + 1
            elif(List[g] == nota[10]):
                frequencys.append('SOUNDS/f2.wav')
                convert.append(dic[nota[10]])
                g = g + 1
            elif(List[g] == nota[11]):
                frequencys.append('SOUNDS/g2.wav')
                convert.append(dic[nota[11]])
                g = g + 1
            elif(List[g] == nota[12]):
                frequencys.append('SOUNDS/a2.wav')
                convert.append(dic[nota[12]])
                g = g + 1
            elif(List[g] == nota[13]):
                frequencys.append('SOUNDS/b2.wav')
                convert.append(dic[nota[13]])
                g = g + 1
            elif(List[g] == nota[14]):
                frequencys.append('SOUNDS/c3.wav')#    C3
                convert.append(dic[nota[14]])
                g = g + 1
            elif(List[g] == nota[15]):
                frequencys.append('SOUNDS/d3.wav')
                convert.append(dic[nota[15]])
                g = g + 1
            elif(List[g] == nota[16]):
                frequencys.append('SOUNDS/e3.wav')
                convert.append(dic[nota[16]])
                g = g + 1
            elif(List[g] == nota[17]):
                frequencys.append('SOUNDS/f3.wav')
                convert.append(dic[nota[17]])
                g = g + 1
            elif(List[g] == nota[18]):
                frequencys.append('SOUNDS/g3.wav')
                convert.append(dic[nota[18]])
                g = g + 1
            elif(List[g] == nota[19]):
                frequencys.append('SOUNDS/a3.wav')
                convert.append(dic[nota[19]])
                g = g + 1
            elif(List[g] == nota[20]):
                frequencys.append('SOUNDS/b3.wav')
                convert.append(dic[nota[20]])
                g = g + 1
            elif(List[g] == nota[21]):
                frequencys.append('SOUNDS/c4.wav')
                convert.append(dic[nota[21]])
                g = g + 1
            else:
                tkinter.messagebox.showinfo(title = 'result', message =  "invalid note was typed")
                break
    string = ','.join(convert)
    tkinter.messagebox.showinfo(title = 'result', message =  string)
    for x in range(len(List)):
        pg.mixer.Sound(frequencys[x]).play()
        time.sleep(1.5)
    print(" ")
                
def ask1():
    return simpledialog.askstring("Input", 'type the file name.(if you have any questions read \"readme.txt\")')

def ask2():
    return simpledialog.askstring("Input", 'type the notes separatedby comma.(if you have any questions read \"readme.txt\")')

def ask3():
    return simpledialog.askstring("Input", 'type the note you want to change(if you have any questions read \"readme.txt\")')

def ask4():
    return simpledialog.askstring("Input", 'type the new simbol(if you have any questions read \"readme.txt\")')
    
def option3():
    nota = p.load()
    sentinel = 0
    h = ask3()
    asn = ask4()
    t = 0
    while(t<len(nota)):
        if(nota[t] == h):
            sentinel = 1
            salvo = t
        t = t+1 
    if(sentinel == 1):
        p.save(salvo,asn)
    else:
        print("couldnt find the note")


def option4():
    nota = p.load()
    string = ','.join(nota)
    tkinter.messagebox.showinfo(title = 'current notes', message =  string)
