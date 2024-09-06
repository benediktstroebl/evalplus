def car_race_collision(n: int):
    # Initialize two lists to represent the positions of cars moving left to right and right to left.
    l2r = [i for i in range(n)]
    r2l = [i for i in range(n)]
    
    # Initialize a variable to track the number of collisions.
    collisions = 0
    
    # Iterate through the positions of the cars moving left to right.
    for i in l2r:
        # Check if there is a car moving right to left at the same position.
        if r2l[i] == i:
            # If the car is at the same position, it has collided, so increment the collision count.
            collisions += 1
        # Shift the position of the car moving right to left to the right (towards increasing positions).
        r2l[i] += 1
    
    return collisions