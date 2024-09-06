def car_race_collision(n: int):
    # Define two lists to hold the positions of left and right driving cars.
    left_driving = [i for i in range(n)]
    right_driving = [i for i in range(n, 2 * n)]

    # Initialize collisions as 0.
    collisions = 0

    # Iterate through all possible pairs of cars.
    for i in range(n - 1):
        for j in range(n - 1):
            # Check if the gap between the cars is closing or if they are coming together.
            if left_driving[i] + right_driving[j] == right_driving[j - 1] - left_driving[i + 1]:
                collisions += 1

    return collisions