def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right driving cars.
    left_driving = [i for i in range(n)]
    right_driving = [i for i in range(n)]

    # Initialize collisions as 0.
    collisions = 0

    # Move left driving cars to the right.
    for i in range(n):
        left_driving[i] += 1

        # Move right driving cars to the left.
        right_driving[i] -= 1

        # Check if a collision occurs.
        if left_driving[i] == right_driving[i]:
            collisions += 1

    return collisions