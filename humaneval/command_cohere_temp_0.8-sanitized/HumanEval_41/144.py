def car_race_collision(n):
    # Initialize two lists to represent the position of each car.
    car_positions = [0] * 2 * n
    moving_left_to_right = [True] * n + [False] * n

    # Each car moving left to right starts at index `2*i` and each car moving right to left starts at index `2*i+1`.
    # The first n cars on the left are moving left to right, so set their initial status accordingly.
    for i in range(n):
        car_positions[2*i] = i  # The index is the position of the car (0-based)
        moving_left_to_right[i] = True

    # The next n cars are moving right to left, so set their status accordingly.
    for i in range(n):
        car_positions[2*i + 1] = i  # The index is the position of the car (0-based)
        moving_left_to_right[n + i] = False

    # Iterate through each pair of cars to check for collisions.
    collisions = 0
    for i in range(2 * n - 1):
        if moving_left_to_right[i] and not moving_left_to_right[i + 1]:
            # If moving_left_to_right[i] is true and moving_left_to_right[i+1] is false,
            # then the car at index i is moving left to right and will collide with the car at index i+1.
            collisions += 1

    return collisions