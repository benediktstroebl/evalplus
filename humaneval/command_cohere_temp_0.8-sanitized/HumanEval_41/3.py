def car_race_collision(n: int):
    # Define 2 lists to store the positions of inward and outward moving cars.
    inward, outward = [0] * n, [0] * n
    
    # Track the number of collisions:
    collisions = 0
    
    # Initialize the position of each car:
    for car_num in range(1, n + 1):
        # Even cars move outward:
        inward[car_num // 2] = -car_num
        
        # Odd cars move inward:
        outward[car_num // 2] = car_num
    
    # Iterate through each car to check for collisions:
    for car_num in range(1, n + 1):
        if inward[car_num] > 0 and outward[car_num] < 0:
            # If an inward moving car finds an empty spot, it moves to that spot:
            inward[car_num] += 1
        elif inward[car_num] < 0 and outward[car_num] > 0:
            # If an outward moving car finds an empty spot, it moves to that spot:
            outward[car_num] += 1
        elif inward[car_num] < 0 and outward[car_num] < 0:
            # If both cars are moving inward or both are moving outward, no collision:
            pass
        else:  # if(inward[car_num] > 0 && outward[car_num] > 0):
            # If a car moving inward hits a car moving outward, mark it as a collision:
            collisions += 1
    
    return collisions