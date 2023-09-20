restaurants = ["In N Out", "Raising Cane's", "Chick Fil A", "McDonalds", "Taco Bell", "Burger King"]

def rankrestaurant(newrestaurant, restaurants):
    for i in range(len(restaurants)):
        rank = input("Do you like A) " + newrestaurant + " or B) " + restaurants[i] + " more? A/B")
        if rank == "A" or rank == "a":
            restaurants.insert(i, newrestaurant)
            break
        elif rank == "B" or rank == "b":
            if i + 1 == len(restaurants):
                restaurants.insert((i + 1), newrestaurant)
    return restaurants

print("Welcome to your restaurant list. Your current restaurant ranking is" + (', '.join(restaurants)) + ".")
addsort = input("Would you like to add a new restaurant or sort your existing restaurants? a/s")

if addsort == "a" or addsort == "A":
    newrestaurant = input("What restaurant would you like to add?")
    print("Your new restaurant ranking is " + (', '.join(rankrestaurant(newrestaurant, restaurants))) + ".")
else:
    oldrestaurants = restaurants
    restaurants = [oldrestaurants[0]]
    del oldrestaurants[0]
    while len(oldrestaurants) != 0:
        rankrestaurant(oldrestaurants[0], restaurants)
        del oldrestaurants[0]
    print("Your new restaurant ranking is " + (', '.join(restaurants)) + ".")
