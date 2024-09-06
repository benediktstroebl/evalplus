def car_race_collision(n):
    # Define two lists to represent the positions of cars moving left to right and right to left.
    l2r = [i for i in range(n)]
    r2l = [i for i in range(n)]
    
    # Initialize variables to track the number of collisions and the current position of cars.
    collisions = 0
    position = 0
    
    while len(l2r) + len(r2l) > 0:
        # Check if the current position is a collision.
        if l2r[position] == r2l[position]:
            collisions += 1
        
        # Move the left-to-right cars to the right and the right-to-left cars to the left.
        for _ in range(n):
            position += 1
            l2r.pop(0) if position >= len(l2r) else None
            r2l.pop(0) if position >= len(r2l) else None
    
    return collisions