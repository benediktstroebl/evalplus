def car_race_collision(n: int):
    """
    Determine the number of collisions when two sets of n cars move towards each other on an infinitely long straight road.
    """
    # Define the two sets of cars as two lists
    cars_1 = [i for i in range(n)]
    cars_2 = [i for i in range(n, 0, -1)]
    
    # Initialize collisions as 0
    collisions = 0
    
    # Compare cars in the two sets to find collisions
    for car_1, car_2 in zip(cars_1, cars_2):
        if car_1 == car_2:
            collisions += 1
    
    return collisions