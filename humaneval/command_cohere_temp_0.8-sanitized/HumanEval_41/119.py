def car_race_collision(n: int):
    # Initialize two lists to keep track of left and right moving cars.
    moving_left = [0] * n
    moving_right = [0] * n

    # Flag to track if a collision happens.
    collision = False

    # Move the cars across the finish line.
    for i in range(n):
        # If there's no car on the right and a car on the left, a collision occurs.
        if not moving_right[i] and moving_left[i]:
            collision = True

        # If a car passes the finish line on either side, mark it as such.
        if i == n - 1 or i == 0:
            moving_left[i] = 1 if i == 0 else 0
            moving_right[i] = 1 if i == n - 1 else 0

        # Toggle cars for the next round.
        if i < n - 1:
            moving_left[i], moving_right[i] = moving_right[i], moving_left[i]

    # If any collision happened during any round, return 1, else return 0.
    return 1 if collision else 0