def car_race_collision(n: int):
    # Define the two groups of cars
    cars1 = [i for i in range(n)]
    cars2 = [i for i in range(n)]
    
    # Define the collision variable
    collisions = 0

    # Iterate through each car in the first group
    for i in cars1:
        # Check if the current car in the first group has a matching car in the second group
        if i == cars2[-1] or i == cars2[0]: 
            collisions += 1
        
        # Move the car in the second group to the right (simulating movement)
        cars2.remove(i)
    
    # Reverse the movement of the second group of cars (simulation)
    cars2.reverse()

    # Iterate through each car in the second group
    for i in cars2:
        # Check if the current car in the second group has a matching car in the first group
        if i == cars1[-1] or i == cars1[0]:
            collisions += 1
        
        # Move the car in the first group to the right (simulation)
        cars1.remove(i)

    return collisions