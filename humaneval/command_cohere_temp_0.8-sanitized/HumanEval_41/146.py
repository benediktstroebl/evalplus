def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right driving cars.
    left_drive = [i for i in range(n)]
    right_drive = [i for i in range(n)]

    # Initialize collisions as 0.
    collisions = 0

    # Iterate until the 2 lists have a different element at the same index.
    while left_drive == right_drive:
        left_drive[0] += 1
        right_drive[0] -= 1

        # If the 2 cars at the same index collide, increment collisions.
        if left_drive[0] == right_drive[0]:
            collisions += 1

    return collisions