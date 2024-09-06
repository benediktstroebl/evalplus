def car_race_collision(n: int):
    # Initialize two lists to represent the positions of cars moving left to right and right to left.
    l2r = [i for i in range(n)]
    r2l = [i for i in range(n)]
    
    # Sort the lists according to the increasing positions of cars.
    l2r.sort()
    r2l.sort(reverse=True)
    
    # Initialize a variable to count the number of collisions.
    collisions = 0
    
    # Iterate through the pairs of cars to check for collisions.
    for i in range(n - 1):
        if l2r[i] == r2l[0]:
            collisions += 1
            r2l.pop(0)
        elif l2r[i] > r2l[0]:
            r2l.pop(0)
    
    return collisions