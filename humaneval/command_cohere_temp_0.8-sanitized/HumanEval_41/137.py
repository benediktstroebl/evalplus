def car_race_collision(n: int):
    # Initialize two lists to hold the positions of left and right driving cars.
    left_drive = [i for i in range(n)]
    right_drive = [i for i in range(n)]

    # Initialize collisions as 0, it will increase when a collision happens.
    collisions = 0

    # Move left cars to the right by n positions.
    for i in range(n):
        left_drive[i] = left_drive[i] + n

    # Find the positions where left and right driven cars intersect.
    for i in range(n):
        if left_drive[i] == right_drive[i]:
            collisions += 1

    return collisions