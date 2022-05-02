# Project: iBike
# Professor: Chaya Rao
# Team: Alexis Sledge-Osimen, Mohammad Hassan, Tung Dinh
# HCC - Summer 2021 - COSC 1437

# =========================================



class Bike:                                   #PARENT CLASS OR SUPERCLASS
  def __init__(self, metal_frame, saddle, brake, wheel, tread):
    self.metal_frame = metal_frame
    self.saddle = saddle
    self.brake = brake
    self.wheel = wheel
    self.tread = tread
 
  def __repr__(self): # This method represents the class
    return self.metal_frame + '; ' + self.saddle + '; ' + self.brake + '; ' + self.wheel +'; ' + self.tread

class Specialized_Bike(Bike):                  #INHERIT CLASS OR SUBCLASS
  def __init__(self, metal_frame, saddle, brake, wheel, tread, helmet, gloves, waterbottleholder):  
    super().__init__(metal_frame, saddle, brake, wheel, tread) #This method is used as a shortcut for parent class attributes.
    #self.metal_frame = metal_frame #These were commented to show future user that this can be used, as well.
    #self.saddle = saddle
    #self.brake = brake
    #self.wheel = wheel
    #self.tread = tread
    self.helmet = helmet #These three attributes were added as additional features for user.
    self.gloves = gloves
    self.waterbottleholder = waterbottleholder
  def __repr__(self):
    return self.metal_frame + '; ' + self.saddle + '; ' + self.brake + '; '  + self.wheel + '; ' + self.tread + '; ' + self.helmet + '; ' + self.gloves + '; ' + self.waterbottleholder


# =========================================
import time
import random

SEC = 3600

def get_customer_info():
    name = input("Please enter your full name: ")
    phone = input("Please enter your phone number: ")
    return name, phone

class Rental_Bike(Bike):
    
    def __init__(self, bike_name, rate):
        self.bike_name = bike_name
        self.rate = rate
        self.borrower = []
        
    def check_out(self):
        self.borrower.append(get_customer_info())
        self.check_out_time = time.time()
        time.sleep(1) # delay time for 1 sec
        print()
        print("Your bike is ready. Enjoy the ride!")
        print(time.asctime(time.localtime(self.check_out_time )))
        
    def check_in(self):
        time.sleep(3) # delay time for 1 sec
        
        while True:
            try:
                self.borrower.remove((get_customer_info()))
                break
        
            except ValueError:
                print("<Customer not found. Please try again>")
                
        self.check_in_time = time.time()
        
        # Simulate time passed
        rand = random.randint(2, 5)
        simulation = SEC*rand
        
        duration = self.check_in_time + simulation - self.check_out_time        
        cost = round(duration/SEC) * self.rate
        
        print()
        print("Thanks for riding our bikes!")
        print("Please pay $" + str(cost))
        print(time.asctime(time.localtime(self.check_in_time + simulation)))


    def __repr__(self):
        return self.bike_name + ": $" + str(self.rate) + "/HOUR" 
    
# =========================================

#INVENTORY AT THE LOCATION
Galleria_inventory = {"EasyRyder100": 2, "ProX100": 2, "EasyRyder200": 2, "ProX200":2}
Kirby_inventory = {"EasyRyder100": 2, "ProX100": 2, "EasyRyder200": 2, "ProX200":2}
Downtown_inventory = {"EasyRyder100": 2, "ProX100": 2, "EasyRyder200": 2, "ProX200":2}
 
#RENTAL LOCATIONS
class Rental_location:
  def __init__ (self, stands, bikes):
    self.stands = stands
    self.bikes = bikes
    # create an attribute that store the number of bikes at the station, initially set to 0, we count later
    self.total_bike = 0

  def locationBikeRent(self, bikechoice): 
    # Check if the selected bike has zero inventory
    if self.bikes[bikechoice] > 0: 
        self.bikes[bikechoice] -= 1
    else:
        print("Error, This bike is not available")
        return False # This raise a flag. It helps later codes able to catch it.

  def locationBikeReturn(self, bikechoice):
    # Counting bikes 
    for bike in self.bikes:
        self.total_bike += self.bikes[bike]

    # Check if the stand is full
    if self.total_bike < self.stands:
        self.bikes[bikechoice] += 1
    else:
        print("Error, This location is full. Please return your bike at the other location")
        print("Thank you!!!!")
        return False  # This raise a flag. It helps later codes able to catch it.


# ----- CREATING INSTANCES -----
# Bikes
EasyRyder100 = Bike('NavyBlueCarbonFiberBikeFrame', 'WideSaddle', 'DiscBrakes', '700Cwheels', 'GravelTread')
ProX100 = Bike('BlackandGoldCarbonFiber', 'WideSaddle', 'DiscBrakes', '700Cwheels', 'GravelTreadandAngledTread')
EasyRyder200 =Specialized_Bike('ClassicRedCarbonFiberBikeFrame', 'WideSaddle', 'DiscBrakes', '700Cwheels', 'GravelTread', 'ClassicRedHelmet', 'ClassicRedGloves', 'WaterBottleHolder')
ProX200 = Specialized_Bike('BlackandClassicRedCarbonFiberBikeFrame', 'WideSaddle', 'DiscBrakes', '700Cwheels', 'GravelTread', 'BlackandClassicRedHelmet', 'BlackandClassicRedGloves', 'WaterBottleHolder')


# Rental bikes
# Mapping each rental bike to a corresponding bike
bikes = {EasyRyder100: Rental_Bike(bike_name = "EasyRyder100", rate = 5), 
         ProX100: Rental_Bike(bike_name = "ProX100", rate = 8), 
         EasyRyder200: Rental_Bike(bike_name = "EasyRyder200", rate = 10), 
         ProX200: Rental_Bike(bike_name = "ProX200", rate = 12)}


# Stations
Galleria = Rental_location(10, Galleria_inventory)
Downtown = Rental_location(10, Downtown_inventory)
Kirby = Rental_location(10, Kirby_inventory)


# ------------------------------
# ----- DEFINING FUNCTIONS -----
def stationChoice():
    print("1. Galleria")
    print("2. Kirby")
    print("3. Downtown")
    stationChoice = input("Please choose a station: ")
    if stationChoice == "1":
      return Galleria
    elif stationChoice == "2":
      return Downtown
    elif stationChoice == "3":
      return Kirby 
    else:
      print("Choose correct option: ")    
   
def bikeChoice():
    #Allows customer to choose which selection they desire
    customer_choice= int(input("""Please select one of the following options:\n1 = EasyRyder100, 2 = ProX100, 3 = EasyRyder200, 4 = ProX200\nEnter a number associated with desired bike selection: """))

    #If/else statement needed to tell customer what is included in their choice.
    if  customer_choice == 1:
        return EasyRyder100
    elif  customer_choice ==  2:
        return ProX100
    elif  customer_choice ==  3:
        return EasyRyder200
    elif  customer_choice ==  4:
        return ProX200

def rent_or_return(station, bike_collection, confirmation = "N"):
    print("\n----- STEP 2: RENT OR RETURN")
    action = input("Are you renting or returning a bike? rent/return ")

    if action == "rent":
        while confirmation == "N":
            # Displaying inventory
            print("\n----- BIKE COLLECTION:")
            print(station.bikes)

            # Displaying the collection of rental bikes with the hour rate
            for bike in bike_collection:
                print(bike_collection[bike]) 

            # Selecting a bike to rent
            print("\n----- STEP 3: SELECT A BIKE")
            bike = bikeChoice() 
            rent_bike = bikes[bike] # Pull the corresponding Rental_Bike based on the selected bike
        
            # Displaying info of the selected bike
            print(f"\n----- YOU SELECTED {rent_bike.bike_name.upper()}")
            print(bike)
            print()

            # Confirming
            print("\n----- STEP 4: CONFIRMATION")
            confirmation = input("Y to accept the bike. N to return to the bike collection. ")

        # Check, update inventory and check out the bike
        if station.locationBikeRent(rent_bike.bike_name) == False:
            pass
        else:
            print("\n----- STEP 5: INPUT INFO")
            rent_bike.check_out()
       


    elif action == "return": 
        # Selecting a bike to return
        print("\n----- STEP 3: SELECT A BIKE")
        return_bike = bikes[bikeChoice()]  

        # Check, update inventory and check out the bike
        if station.locationBikeReturn(return_bike.bike_name) == False:
            pass
        else:
            print("\n----- STEP 4: INPUT INFO")
            return_bike.check_in()

# ------------------------------
# ----- ***MAIN PROGRAM*** -----
while True:
    print("\n\n-----WELCOME TO iBIKE-----\n")

    # Select a location
    print("\n----- STEP 1: LOCATION")
    station = stationChoice()
    
    # Choosing rent or return  
    rent_or_return(station, bikes)

    time.sleep(5) # delay time for 5 sec

        
