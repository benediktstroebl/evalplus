def car_race_collision(n: int):
    # Initialize two lists to hold the positions of the left and right driving cars.
    left_driving = [i for i in range(n)]
    right_driving = [i for i in range(n)]

    # Initialize collisions as 0, which is the number of collisions.
    collisions = 0

    # Iterate through each pair of cars.
    for i in range(n - 1):
        # If the left car is less than the right car, they haven't collided.
        if left_driving[i] < right_driving[i]:
            continue

        # If the left car is greater than or equal to the right car, they have collided.
        collisions += 1

        # Move the right car.
        right_driving[i + 1] = right_driving[i] + 1

    return collisions