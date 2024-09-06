def car_race_collision(n: int):
    """
    Determine the number of collisions when two sets of n cars move in opposite directions on an infinitely long straight road.
    """
    collisions = 0
    
    # Define two sets of cars along the same straight path
    cars1 = ['A' + str(i) for i in range(n)]
    cars2 = ['B' + str(i) for i in range(n)]
    
    # Reverse the second set of cars for collision detection
    cars2.reverse()
    
    # Check for collisions between the two sets
    for car1 in cars1:
        for car2 in cars2:
            if car1 == car2:
                collisions += 1
                break  # Move on to the next car in cars1
    
    return collisions