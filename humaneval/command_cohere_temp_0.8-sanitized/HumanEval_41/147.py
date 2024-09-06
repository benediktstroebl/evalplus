def car_race_collision(n: int):
    # Initialize two lists to represent the positions of cars moving left to right and right to left.
    l2r = [i for i in range(n)]
    r2l = [i for i in range(n)]
    
    # Initialize a variable to track the number of collisions.
    collisions = 0

    # Iterate through the positions of the cars moving left to right.
    for i in l2r:
        # Check if there is a car moving right to left at the same position.
        if i in r2l:
            # If there is, mark a collision and increment the count.
            collisions += 1
            r2l.remove(i)
    
    # Reverse the r2l list and repeat the loop to check for collisions in both directions.
    for i in r2l:
        if i in l2r:
            collisions += 1
            l2r.remove(i)
    
    return collisions