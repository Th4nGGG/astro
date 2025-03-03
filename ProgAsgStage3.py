##Author: Thang Duc Phung
##Student ID: 3206198
##Programming Assignment 4478
##Date created: 16 Oct 2019
##Date last changed: 20 Oct 2019
##This program reading an external text file(astronaut.txt) and display data using GUI (tkinter)


from tkinter import *

##Constants
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400
COLOR = 'lightblue'
PADDING = 30
X_BAR_0, Y_BAR_0 = 20,349  ##For bars in the chart
X_TEXT = 30                ##For labels in the chart
MASS_CREW = 100
MASS_SPECIALIST = 150

##A list to store data from text file
astroList = list()
astroMass = list()

##Variables
mass_mul=""
mass=""

##Main function
def main():
    file = "astronaut.txt"
    readfile()

##Function that returns the second element of a single list (which is mass multiplier)
def secondElement(var):
    return var[1]
    
##This function will read the file and store the data in a list
def readfile():
    infile = open("astronaut.txt",'r')
    line = infile.readline()
    while line != "":
        astroLine = tuple()
        astroLine = (line.strip().split(","))
        astroList.append(astroLine)
        line = infile.readline()
    infile.close()   
    astroList.sort(key = secondElement)
    
##Create a list for listbox widget        
def displayDestination():
    lstPlanet = ""
    for planet in astroList:
        lstPlanet += planet[0]+"\n"
    lstDestination.set(lstPlanet)

##Display planet's  mass multiplier when click on the listbox
def displayMassMultiplier(event):
    global mass_mul, astroMass
    selectedPlanet = lstDes.get(lstDes.curselection())
    selectedPlanetIndex = lstDes.get(0, "end").index(selectedPlanet)
    mass_mul = float(astroList[selectedPlanetIndex][1])  ##Get mass multiplier from the nested list
    txtMassMul.set("Mass Multiplier: " + str(mass_mul))
    astroMass = astroList[selectedPlanetIndex][2:8]  ##List of astronauts mass
    
##Draw a chart to compare mass multipliers
def canvasDraw():
    global X_BAR_0, Y_BAR_0, X_TEXT
    canvas.create_text(300,40, text="Mass Multiplier", font="Serif 15 bold")
    canvas.create_text(20,15,text="1")
    canvas.create_text(20,180,text="0.5")
    canvas.create_line(10,10,10,350,width=2)
    canvas.create_line(10,350,600,350,width=2)
    for i in range(0,len(astroList)):
        x = float(astroList[i][1])
        x_bar_1 = X_BAR_0 + PADDING
        y_bar_1 = Y_BAR_0 - x*300
        canvas.create_rectangle(X_BAR_0, Y_BAR_0,
                                x_bar_1, y_bar_1, fill=COLOR) ##Create bars
        X_BAR_0 += 60
        x_bar_1 += 60
        canvas.create_text(X_TEXT,360, text=astroList[i][0],
                           font="Calibri 10")     ##Create different labels for planets
        X_TEXT += 60
        
##Display astronauts mass and do calculations
def displayAstroMass():
    global astroMass
    astro1.set(astroMass[0])     ##Assign variables to entry widgets
    astro2.set(astroMass[1])
    astro3.set(astroMass[2])
    astro4.set(astroMass[3])
    astro5.set(astroMass[4])
    astro6.set(astroMass[5])
    crew1 = int(astroMass[0])    ##Convert to integer for calculation
    crew2 = int(astroMass[1])
    crew3 = int(astroMass[2])
    spec1 = int(astroMass[3])
    spec2 = int(astroMass[4])
    spec3 = int(astroMass[5])
    available1 = MASS_CREW - crew1
    available2 = MASS_CREW - crew2
    available3 = MASS_CREW - crew3
    available4 = MASS_SPECIALIST - spec1
    available5 = MASS_SPECIALIST - spec2
    available6 = MASS_SPECIALIST - spec3
    lst = [available1,available2,available3,       ##A list to make calculation easier
          available4,available5,available6]
    avg_mass = sum(lst)/6
    avg_weight = avg_mass * mass_mul
    avgMass.set("Average Mass is: {:.5f} kg".format(avg_mass))
    avgWeight.set("Average Weight on your destination is: {:.5f} kg".format(avg_weight))
    
main()

##GUI part
window = Tk()
window.title("Astronaut - Stage 3")

##Button to display planets and its mass multiplier
btnPlanet = Button(window, text="Display destinations", command=displayDestination, bg=COLOR)
btnPlanet.grid(row=0,column=0, padx=10, pady=10)

##Button to display a graph
btnDraw = Button(window, text = "Compare Mass Multiplier",command=canvasDraw, bg=COLOR)
btnDraw.grid(row=0,column=2,padx=10, pady=10)

#Button to display mass
btnDisplay = Button(window, bg=COLOR,text="Display astronauts mass",command=displayAstroMass)
btnDisplay.grid(row=1, column=0, sticky=S, pady=5)

##A list box to display planets
lstDestination = StringVar()
lstDes = Listbox(window, width=20, height=10, listvariable=lstDestination)
lstDes.grid(row=1, column=0, rowspan=6, sticky=N, padx=10)
lstDes.bind("<<ListboxSelect>>",displayMassMultiplier)

##Entry widget for display
txtMassMul = StringVar()
entMassMul = Entry(window, state="readonly", textvariable=txtMassMul)
entMassMul.grid(row=1,column=0, sticky=W, padx=10)

##Canvas for creating a graph
canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.grid(row=1, column=2, padx =10, pady=(0,10))

##Lables 
for i in range(0,6):
    Label(window, text = "Astronaut " + str(i+1), font="Calibri 10 bold").grid(row = 3+i , column = 0, sticky=W)
        
##Display mass for astronauts
astro1 = StringVar()
entAstro1 = Entry(window, width=10,textvariable = astro1,state="readonly")
entAstro1.grid(row=3, column=0, padx=5, pady=5, sticky=E)

astro2 = StringVar()
entAstro2 = Entry(window, width=10,textvariable = astro2,state="readonly")
entAstro2.grid(row=4, column=0, padx=5, pady=5, sticky=E)

astro3 = StringVar()
entAstro3 = Entry(window, width=10,textvariable = astro3,state="readonly")
entAstro3.grid(row=5, column=0, padx=5, pady=5, sticky=E)

astro4 = StringVar()
entAstro4 = Entry(window, width=10,textvariable = astro4,state="readonly")
entAstro4.grid(row=6,column=0, padx=5, pady=5, sticky=E)

astro5 = StringVar()
entAstro5 = Entry(window, width=10,textvariable = astro5,state="readonly")
entAstro5.grid(row=7,column=0, padx=5, pady=5, sticky=E)

astro6 = StringVar()
entAstro6 = Entry(window, width=10,textvariable = astro6,state="readonly")
entAstro6.grid(row=8,column=0, padx=5, pady=5, sticky=E)

avgMass = StringVar()
entAvgMass = Entry(window, width=48, textvariable = avgMass, state = "readonly" )
entAvgMass.grid(row=3, column=2,padx = 10, pady = 10, sticky=W)

avgWeight = StringVar()
entAvgWeight = Entry(window, width=48,state = "readonly", textvariable = avgWeight)
entAvgWeight.grid(row=3, column=2,padx = 10, pady = 10, sticky=E)

window.mainloop()
