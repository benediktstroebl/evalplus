def car_race_collision(n: int):
    """
    Determine the number of collisions when two sets of n cars drive towards each other on an infinitely long straight road.
    """
    # Define variables
    collisions = 0
    total_cars = 2 * n
    
    # Calculate the number of collisions
    for i in range(1, total_cars):
        if i + total_cars >= 2 * n:
            collisions += 1
    
    return collisions