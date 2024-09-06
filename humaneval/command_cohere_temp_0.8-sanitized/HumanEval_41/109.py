def car_race_collision(n: int):
    """
    Determine the number of collisions when two sets of n cars move towards each other on an infinitely long straight road.
    """
    # Define the two sets of cars as two lists of n cars each.
    cars_1 = [i for i in range(n)]
    cars_2 = [i for i in range(n, 0, -1)]
    
    # Initialize the collision count to zero.
    collision_count = 0
    
    # Iterate over the two sets of cars and check for collisions.
    for i in cars_1:
        for j in cars_2:
            if i > j:
                collision_count += 1
                break  # Move on to the next iteration of the inner loop.
    
    return collision_count