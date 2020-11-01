# CIS 245 Week 8 Car Assignment

class Vehicle:
    def __init__(self):
        #Initialize Vehicle Attributes

        self.make = "make"
        self.model = "model"
        self.color = "color"
        self.fuelType = "fuelType"
        self.options = 0
        self.optionsList = ["1: cruise control", "2: bluetooth", "3: heated seats", "4: backup camera", "5: premium audio system", "6: leather seats", "7: navigation package", "8: self-park\n"]

    def getMake(self):
        self.make = str(input("What's the make of your vehicle?\n"))

    def getModel(self):
        self.model = input("What's the model of your vehicle?\n")

    def getColor(self):
        self.color = input("Enter the color of your vehicle:\n")

    def getfuelType(self):
        self.fuelType = input("Is your vehicle gasoline, diesel, hybrid, or electric?\n")

    def getOptions(self):
        print(self.optionsList)
        inputOptions = input("Please select the options you'd like to include for your vehicle.\n")
        self.options = self.optionsList[inputOptions - 1]
        print(self.options)

class Car(Vehicle):
    def __init__(self):
         Vehicle.__init__(self)

         self.engineSize = 0.0
         self.numDoors = 0

        #Initialize Car Attributes
    def getengineSize(self):
        print(self.engineSize)
        engineSize = float(input("What engine size will your car have?"))


    def getnumDoors(self):
        print(self.numDoors)
        numDoors = [4, 2]
        numDoors = int(input("How many doors will your car have?"))
        if numDoors != 4 or 2:
            print("Sorry, your vehicle can have either two doors or four. Please try again.")


class Pickup(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)

        #Initialize Pickup Attributes
    def getcabStyle(self):
        print(self.cabStyle)

    def bedLength(self):
        print(self.bedLength)

addVehicle = True
counter = 0

myGarage = []
vehicleChoice = 0

while addVehicle:

    vehicleChoice = int(input("Car (1) or Truck (2) or None (3)\n"))
    if vehicleChoice == 1:
        myGarage.append(Car())
        myGarage[counter].getMake()
        myGarage[counter].getModel()
        print("Car added to Garage.\n")
    elif vehicleChoice == 2:
        myGarage.append(Pickup())
        myGarage[counter].getMake()
        myGarage[counter].getModel()
        print("Truck added to Garage.\n")
    else:
        addVehicle = False

    counter += 1

x = 0
while x < len(myGarage):
    print(myGarage[x].make)
    print(myGarage[x].model)
    x += 1
