def car_race_collision(n: int):
    # Initialize two lists to represent the positions of cars moving left to right and right to left.
    l2r = [i for i in range(n)]
    r2l = [i for i in range(n)]
    
    # Sort the lists according to car positions. Cars moving left to right will have increasing positions,
    # while cars moving right to left will have decreasing positions.
    l2r.sort()
    r2l.sort(reverse=True)
    
    collisions = 0
    # Iterate through the two lists and check if any elements are equal, indicating a collision.
    for i in range(n - 1):
        if l2r[i] == r2l[i]:
            collisions += 1
    
    return collisions