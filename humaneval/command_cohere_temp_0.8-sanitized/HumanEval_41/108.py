def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right driving cars.
    left_drive = [i for i in range(n)]
    right_drive = [i for i in range(n)]
    
    # Initialize the collisions counter.
    collisions = 0

    # Iterate until the 2 lists have converged to the same element at the same index.
    for i in range(n):
        # If cars collide, increase the counter.
        if left_drive[i] == right_drive[i]:
            collisions += 1
        # If a left-driving car is encountered, shift it to the right.
        elif left_drive[i] > right_drive[i]:
            left_drive[i] += 1
        # If a right-driving car is encountered, shift it to the left.
        else:
            right_drive[i] -= 1

    # Return the number of collisions.
    return collisions