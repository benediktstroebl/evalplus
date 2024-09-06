def car_race_collision(n: int):
    # Define two lists to store car positions for each group
    cars_left_to_right = [i for i in range(n)]
    cars_right_to_left = [i for i in range(n)]

    # Define a variable to track collisions
    collisions = 0

    # Iterate through each car in the left-to-right group
    for i in range(n):
        # Check if any cars in the right-to-left group is at the same position or greater
        if cars_right_to_left[i] == i or cars_right_to_left[i] >= i + 1:
            collisions += 1

        # Increment the position of the car in the left-to-right group
        cars_left_to_right[i] += 1

    # Iterate through each car in the right-to-left group
    for i in range(n):
        # Check if any cars in the left-to-right group is at the same position or greater
        if cars_left_to_right[i] == i or cars_left_to_right[i] >= i + 1:
            collisions += 1

        # Increment the position of the car in the right-to-left group
        cars_right_to_left[i] += 1

    return collisions