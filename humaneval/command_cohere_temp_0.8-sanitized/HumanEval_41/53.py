def car_race_collision(n: int):
    """
    Determine the number of collisions when two sets of n cars move toward each other on an infinitely long straight road.
    """
    collisions = 0
    
    # Calculate all possible pairs of cars
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the distance moved by each car in one time step
            car1_distance = i * 2
            car2_distance = n - j + 1
            # Count collisions if distances overlap
            if car1_distance <= car2_distance:
                collisions += 1
            elif car2_distance <= car1_distance:
                collisions += 1
    
    return collisions