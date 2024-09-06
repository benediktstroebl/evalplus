def car_race_collision(n):
    # Define two lists to represent the positions of cars moving left to right and right to left.
    l2r = [i for i in range(n)]
    r2l = [i for i in range(n)]
    
    # Initialize pointers for the positions of the two groups of cars.
    l2r_idx, r2l_idx = 0, n - 1
    
    # Count the number of collisions.
    collisions = 0
    
    while l2r_idx < n and r2l_idx > 0:
        if l2r[l2r_idx] == r2l[r2l_idx]:
            collisions += 1
        l2r_idx += 1
        r2l_idx -= 1
    
    return collisions