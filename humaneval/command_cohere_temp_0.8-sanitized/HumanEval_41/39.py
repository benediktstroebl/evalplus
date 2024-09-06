def car_race_collision(n):
    """
    Determine the number of collisions when two sets of n cars move towards each other on an infinitely long straight road.
    """
    collisions = 0
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n:  # Avoid same car or if car from opposite direction is last car
                continue
            collisions += (i + j) % 2  # Count collisions when car noses pass each other
    return collisions