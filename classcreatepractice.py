restaurants = ["In N Out", "Raising Cane's", "Chick Fil A", "McDonalds", "Taco Bell", "Burger King"]

print("Welcome to your restaurant list. Your current restaurant ranking is" + str(restaurants) + ".")
newrestaurant = input("What restaurant would you like to add?")

def rankrestaurant(newrestaurant, restaurants):
    for i in range(len(restaurants)):
        rank = input("Do you like A) " + newrestaurant + " or B) " + restaurants[i] + " more? A/B")
        if rank == "A" or rank == "a":
            restaurants.insert(i, newrestaurant)
            break
        elif rank == "B" or rank == "b":
            continue
    return restaurants

print("Your current restaurant ranking is" + str(rankrestaurant(newrestaurant, restaurants)) + ".")