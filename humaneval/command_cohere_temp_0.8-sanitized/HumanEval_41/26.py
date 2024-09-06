def car_race_collision(n: int):
    # Initialize two lists to represent the positions of left and right driving cars.
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n, 2 * n)]

    # Iterate through all possible pairs of cars.
    for i in range(n - 1):
        # For each pair of cars, check if they collide.
        if left_cars[i] == right_cars[i]:
            return i + 1  # Collision occurs when a left-driving car matches a right-driving car.

    # If no collisions, return 0.
    return 0