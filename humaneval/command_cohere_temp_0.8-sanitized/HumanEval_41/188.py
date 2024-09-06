def car_race_collision(n: int):
    # Initialize two lists to keep track of left and right moving cars
    moving_left = [False] * n
    moving_right = [False] * n

    # Loop through all possible car pairs
    for i in range(n):
        for j in range(i + 1, n):
            if not moving_left[i] and not moving_right[j]:
                # If two cars collide, mark them as having collided
                moving_left[i] = True
                moving_right[j] = True
                break

    # Count the number of collisions and return the result
    count = sum(1 for i in range(n) if moving_left[i] and moving_right[i])
    return count