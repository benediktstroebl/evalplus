def car_race_collision(n: int):
    # Define two lists to hold the positions of left and right moving cars
    left_cars = [0] * n
    right_cars = [0] * n

    # Define a variable to track collisions
    collisions = 0

    # Assuming n is even for simplicity (showcases the worst case scenario)
    # Cars occupy every 2nd position in each direction
    for i in range(n // 2):
        # Move left cars to the right
        left_cars[i] = left_cars[i] + 1

        # Move right cars to the left
        right_cars[i] = right_cars[i] - 1

        # Check for collisions
        if left_cars[i] == right_cars[i]:
            collisions += 1

    # Return the number of collisions
    return collisions