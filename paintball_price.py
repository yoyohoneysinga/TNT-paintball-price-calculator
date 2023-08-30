def calculate_cost(total_paintballs, people, day, memberships, own_equipment):
    price = 0
    gear_rental = 35 * people
    
    if memberships > 0:
        gear_rental -= 35 * memberships
    if own_equipment > 0:
        gear_rental -= 5 * own_equipment
    
    if day == "Weekend":
        if people <= 10:
            price = 529
            if people > 10:
                price += 35 * (people - 10)
            paintballs = 2000
        elif 20 <= people <= 60:
            price = 529
            if people > 10:
                price += 35 * (people - 10)
            paintballs = 0
    elif day == "Weekday":
        if 6 <= people <= 10:
            price = 350
        else:
            print("Error: Invalid number of people for a weekday.")
            return None, None
    
    remaining_paintballs = total_paintballs - paintballs
    while remaining_paintballs > 0:
        if remaining_paintballs >= 2000:
            price += 142.86
            remaining_paintballs -= 2000
        elif remaining_paintballs >= 500:
            price += 40.18
            remaining_paintballs -= 500
        else:
            price += 8.93
            remaining_paintballs -= 100
            
    price *= 1.12
    total_price = price + gear_rental
    cost_per_player = round(total_price / people, 2)
    paintballs_per_player = round(total_paintballs / people)
    
    return cost_per_player, paintballs_per_player, total_price

people = int(input("How many people are playing: "))
total_paintballs = int(input("Total number of paintballs: "))
day = input("Weekend or Weekday: ").capitalize()
memberships = int(input("How many people have memberships: "))
own_equipment = int(input("How many people have their own equipment: "))

cost_per_player, paintballs_per_player, total_price = calculate_cost(total_paintballs, people, day, memberships, own_equipment)

if cost_per_player is not None:
    print(f"Each player will have to pay ${cost_per_player:.2f} and will get {paintballs_per_player} paintballs.")
    print(f"The total price for the group is ${total_price:.2f}.")
