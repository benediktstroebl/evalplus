def car_race_collision(n):
    # Initialize two lists to hold the positions of left-moving and right-moving cars
    moving_left = [0] * n
    moving_right = [0] * n

    # Define a variable to track the number of collisions
    collisions = 0

    # Iterate through each car in the collision
    for car in range(n):
        # Move the right-moving cars to the right and the left-moving cars to the left
        moving_right[car] += 1
        moving_left[n - 1 - car] += 1

        # Check for collisions
        if moving_right[car] > moving_left[n - 1 - car]:
            collisions += 1

        # Reset the position of the left-moving and right-moving cars for the next iteration
        moving_right[car] = 0
        moving_left[n - 1 - car] = 0

    return collisions