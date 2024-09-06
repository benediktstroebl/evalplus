def car_race_collision(n: int):
    # Initialize two lists to represent the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize collisions as a boolean list with n elements set as False
    collisions = [False for i in range(n)]
    
    # Set the left moving cars to their index + 1, simulating their movement
    for car in left_cars:
        car += 1
    
    # Loop through the left moving cars and compare them with the right moving cars
    for i in range(n):
        if not collisions[i] and left_cars[i] == right_cars[i]:
            collisions[i] = True
    
    # Return the number of collisions
    return sum(collisions)