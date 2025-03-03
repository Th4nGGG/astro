##Author: Thang Duc Phung
##Student ID: 3206198
##Programming Assignment 4478
##Date created: 6 Oct 2019
##Date last changed: 10 Oct 2019
##This program calculates the mass and weight for astronauts on different celestial bodies


##Nested list
celestial_mass_multiplier = [["Mercury",0.378],["Venus",0.907],["Moon",0.166],["Mars",0.377],
                             ["Io",0.1835],["Europa",0.1335],["Ganymede",0.1448],["Callisto",0.1264]]

##Constants
##Max weight for astronauts
MASS_CREW = 100
MASS_SPECIALIST = 150
#Mass multiplier for each destination
MERCURY = 0.378
VENUS = 0.907
MOON = 0.166
MARS = 0.377
IO = 0.1835
EUROPA = 0.1335
GANYMEDE = 0.1448
CALLISTO = 0.1264

##Variable
choice = ""
lst = []
destination = ""
mass_mul = ""
avg_mass = ""
avg_weight = ""

##Main function 
def main():
    while True:        
        choice = printMenu()
        if choice == "A":
            displayProgOptions()
        elif choice == "B":
            displayDesWithMass()
        elif choice == "C":
            displayWeightAllowance()        
        elif choice == "D":
            getWeight()
            calculatePersonalMass()     
        elif choice == "E":
            getWeight()
            calculateAverageMassWeight()
        elif choice == "X":
            exit()
        else:
            print("Try again!")
            
##Print out a menu 
def printMenu():
    print( "-"*10, "Astronaut Mass Calculator", "-"*10 )
    print("A: Display Program options")
    print("B: Display Destinations with Mass Multipliers")
    print("C: Display Weight allowances for astronauts")
    print("D: Calculate Personal Mass allowances")
    print("E: Calculate Average Available mass and weight")
    print("X: exit")
    choice = input("Choose a program: ").upper()
    return choice

##Print all the program options
def displayProgOptions():
    print("Display Destinations with Mass Multipliers")
    print("Display Weight allowances for astronauts")
    print("Calculate Personal Mass allowances")
    print("Calculate Average Available mass and weight")
       
##Print celestial bodies with their mass multipliers
def displayDesWithMass():
    for x in celestial_mass_multiplier:
        print("Destination: {0:<12} Mass Multiplier: {1:^10}".format(x[0],x[1]))
       
##Display weight allowances for astronauts
def displayWeightAllowance():
    print("Weight allowance for flight crew is: ", MASS_CREW,"kg")
    print("Weight allowance for mission specialist is: ", MASS_SPECIALIST,"kg")
   
##Insert tool weights
##This function will support both program D and E
def getWeight():
    global lst                  ## Use for function D and E
    crew_1 = float(input("Enter tool weight for 1 crew: "))
    crew_2 = float(input("Enter tool weight for 1 crew: "))
    crew_3 = float(input("Enter tool weight for 1 crew: "))
    spec_1 = float(input("Enter tool weight for 1 specialist: "))
    spec_2 = float(input("Enter tool weight for 1 specialist: "))
    spec_3 = float(input("Enter tool weight for 1 specialist: "))
    available_crew_1 = MASS_CREW - crew_1
    available_crew_2 = MASS_CREW - crew_2
    available_crew_3 = MASS_CREW - crew_3
    available_spec_1 = MASS_SPECIALIST - spec_1
    available_spec_2 = MASS_SPECIALIST - spec_2
    available_spec_3 = MASS_SPECIALIST - spec_3
    lst = [available_crew_1, available_crew_2, available_crew_3,
           available_spec_1, available_spec_2, available_spec_3]
    return lst

##Calculate personal mass for astronauts
def calculatePersonalMass():
    print()                      ##Create a blank line for formatting purpose
    print("Available mass for crew: ")
    print(lst[0], lst[1], lst[2],"", sep="kg\n")
    print("Available mass for specialist: ")
    print(lst[3], lst[4], lst[5],"", sep="kg\n")
    ##A shortcut to next function to make the program more dynamic
    option = input("Do you want to move to next program (E) straightaway [y/n]: ")
    if option.upper() == "Y":
        calculateAverageMassWeight()
    else:
        exit()

##Let user enter destination and the function will calculate average mass and weight on destination      
def calculateAverageMassWeight():
    ##Print out all destination choices
    print("\n1.Mercury","2.Venus","3.Moon","4.Mars","5.Io","6.Europa","7.Ganymede","8.Callisto",sep="\n")
    ##Get mass multiplier of the chosen celestial body
    destination = input("Choose a destination for your mission: ")
    if destination == "1":
        mass_mul = MERCURY
    elif destination == "2":
        mass_mul = VENUS
    elif destination == "3":
        mass_mul = MOON
    elif destination == "4":
        mass_mul = MARS
    elif destination == "5":
        mass_mul = IO
    elif destination == "6":
        mass_mul = EUROPA
    elif destination == "7":
        mass_mul = GANYMEDE
    elif destination == "8":
        mass_mul = CALLISTO
    else:
        print("Your input isn't valid. \nTry again")
    ##Calculate average mass and its weight on the destination
    avg_mass = sum(lst) /6
    avg_weight = mass_mul * avg_mass
    print("Average mass available for the trip is:", avg_mass, "kg")
    print("Average weight available on your destination is: ", avg_weight, "kg")
    

main()


