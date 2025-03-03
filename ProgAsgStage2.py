##Author: Thang Duc Phung
##Student ID: 3206198
##Programming Assignment 4478
##Date created: 8 Oct 2019
##Date last changed: 20 Oct 2019
##This program calculates the mass and weight for astronauts on different celestial bodies using GUI (tkinter)

##Constants
HEIGHT = 4
WIDTH_TEXT = 25
WIDTH_NUMBER = 6
MASS_CREW = 100
MASS_SPECIALIST = 150

##Mass multipliers for each celestial body
MERCURY = 0.378
VENUS = 0.907
MOON = 0.166
MARS = 0.377
IO = 0.1835
EUROPA = 0.1335
GANYMEDE = 0.1448
CALLISTO = 0.1264

##Get mass multiplier for selected celestial body
def getMassMultiplier(event):
   global mass_mul
   selectedPlanet = lstDestination.get(lstDestination.curselection())
   if selectedPlanet == "Mercury":
      mass_mul = MERCURY
   if selectedPlanet == "Venus":
      mass_mul = VENUS
   if selectedPlanet == "Moon":
      mass_mul = MOON
   if selectedPlanet == "Mars":
      mass_mul = MARS
   if selectedPlanet == "Io":
      mass_mul = IO
   if selectedPlanet == "Europa":
      mass_mul = EUROPA
   if selectedPlanet == "Ganymede":
      mass_mul = GANYMEDE
   if selectedPlanet == "Callisto":
      mass_mul = CALLISTO
   massMultiplier.set("Mass multiplier on " + selectedPlanet+ " is: "+ str(mass_mul)) ##Display mass multuplier on screen
    
##Calculate personal mass for astronauts
def calculate():
   astro1=eval(crew_1.get())       ##Store input from entry widgets
   astro2=eval(crew_2.get())
   astro3=eval(crew_3.get())
   astro4=eval(spec_1.get())
   astro5=eval(spec_2.get())
   astro6=eval(spec_3.get())  
   available1 = MASS_CREW - astro1
   available2 = MASS_CREW - astro2
   available3 = MASS_CREW - astro3
   available4 = MASS_SPECIALIST - astro4
   available5 = MASS_SPECIALIST - astro5
   available6 = MASS_SPECIALIST - astro6
   available_crew_1.set(available1)      ##Return variables for mass results
   available_crew_2.set(available2)
   available_crew_3.set(available3)
   available_spec_1.set(available4)
   available_spec_2.set(available5)
   available_spec_3.set(available6)
   lst = [available1,available2,available3,       ##A list to make calculation easier
          available4,available5,available6]
   avg_mass = sum(lst)/6
   avg_weight = avg_mass * mass_mul
   avgMass.set("Average Mass is: {:.5f} kg".format(avg_mass))
   avgWeight.set("Average Weight on your destination is: {:.5f} kg".format(avg_weight))

##GUI program
from tkinter import*
window = Tk()
window.title("Stage2 - Astronaut Mass Calculator")

##Display all elements    
Label(window, text = "Destinations", width = WIDTH_TEXT, height = HEIGHT, font=("Calibri",16)).grid(row=0,column=0)
Label(window, text = "Max Tool Weights", width = WIDTH_TEXT, height = HEIGHT, font=("Calibri",16)).grid(row=0,column=1)
Label(window, text = "Tool Weights", width = WIDTH_TEXT, height = HEIGHT, font=("Calibri",16)).grid(row=0 ,column=2)
Label(window, text = "Available", width = WIDTH_TEXT, height = HEIGHT, font=("Calibri",16)).grid(row=0,column=3)
Label(window, text = "Crew: 100kg", width = WIDTH_TEXT).grid(row=1, column=1)
Label(window, text = "Mission Specialist: 150kg", width=WIDTH_TEXT).grid(row=2, column=1)

##List box for different planets
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=1,column=0,rowspan=4,sticky=NS,padx=(90,0))
destinationList = ["Mercury","Venus","Moon","Mars","Io","Europa","Ganymede","Callisto"]
conOFlstDestination = StringVar()
lstDestination = Listbox(window, width=12, height=6, listvariable=conOFlstDestination,
                    yscrollcommand=yscroll.set)
lstDestination.grid(row=1,column=0, rowspan=4,sticky=W,padx=(100,0))
conOFlstDestination.set(tuple(destinationList))
lstDestination.bind("<<ListboxSelect>>", getMassMultiplier)
yscroll["command"] = lstDestination.yview

##Entry widgets for astronauts tool weights
crew_1 = StringVar()
entCrew1 = Entry(window, width=WIDTH_NUMBER,textvariable = crew_1)
entCrew1.grid(row=1, column=2, padx=5, pady=5)

crew_2 = StringVar()
entCrew2 = Entry(window, width=WIDTH_NUMBER,textvariable = crew_2)
entCrew2.grid(row=2, column=2, padx=5, pady=5)

crew_3 = StringVar()
entCrew3 = Entry(window, width=WIDTH_NUMBER,textvariable = crew_3)
entCrew3.grid(row=3, column=2, padx=5, pady=5)

spec_1 = StringVar()
entSpec1 = Entry(window, width=WIDTH_NUMBER,textvariable = spec_1)
entSpec1.grid(row=4,column=2, padx=5, pady=5)

spec_2 = StringVar()
entSpec2 = Entry(window, width=WIDTH_NUMBER,textvariable = spec_2)
entSpec2.grid(row=5,column=2, padx=5, pady=5)

spec_3 = StringVar()
entSpec3 = Entry(window, width=WIDTH_NUMBER,textvariable = spec_3)
entSpec3.grid(row=6,column=2, padx=5, pady=5)

##Available mass results
available_crew_1 = StringVar()
entAvailableCrew1 = Entry(window,width=WIDTH_NUMBER,textvariable = available_crew_1, state = "readonly" )
entAvailableCrew1.grid(row=1 ,column=3, padx=5, pady=5)

available_crew_2 = StringVar()
entAvailableCrew2 = Entry(window,width=WIDTH_NUMBER,textvariable = available_crew_2, state = "readonly" )
entAvailableCrew2.grid(row=2 ,column=3, padx=5, pady=5)

available_crew_3 = StringVar()
entAvailableCrew3 = Entry(window,width=WIDTH_NUMBER,textvariable = available_crew_3, state = "readonly" )
entAvailableCrew3.grid(row=3 ,column=3, padx=5, pady=5)

available_spec_1 = StringVar()
entAvailableSpec1 = Entry(window,width=WIDTH_NUMBER,textvariable = available_spec_1, state = "readonly" )
entAvailableSpec1.grid(row=4 ,column=3, padx=5, pady=5)

available_spec_2 = StringVar()
entAvailableSpec2 = Entry(window,width=WIDTH_NUMBER,textvariable = available_spec_2, state = "readonly" )
entAvailableSpec2.grid(row=5 ,column=3, padx=5, pady=5)

available_spec_3 = StringVar()
entAvailableSpec3 = Entry(window,width=WIDTH_NUMBER,textvariable = available_spec_3, state = "readonly" )
entAvailableSpec3.grid(row=6 ,column=3, padx=5, pady=5)

##Display mass multiplier of chosen destination
massMultiplier = StringVar()
entMassMultiplier = Entry(window, textvariable=massMultiplier, state = "readonly")
entMassMultiplier.grid(row = 9, column=0, padx = 10, pady = 10, sticky=NSEW,rowspan=2)

##Average mass and weight results
avgMass = StringVar()
entAvgMass = Entry(window, textvariable = avgMass, state = "readonly" )
entAvgMass.grid(row=9, column=1,padx = 10, pady = 10, sticky=NSEW)

avgWeight = StringVar()
entAvgWeight = Entry(window,width=50,state = "readonly", textvariable = avgWeight)
entAvgWeight.grid(row=9, column=2,padx = 10, pady = 10, sticky=NSEW)

##Calculate and Exit buttons
btnCalculate = Button(window, width=12, bg="lightblue", text="Calculate",font=("Calibri",10), command = calculate)
btnCalculate.grid(row=7, column=1, padx = 10, pady = 10)

btnExit = Button(window, width=12, bg="lightblue",text="Exit",font=("Calibri",10), command = exit)
btnExit.grid(row=8, column=1, padx = 10, pady = 10)

window.mainloop()



