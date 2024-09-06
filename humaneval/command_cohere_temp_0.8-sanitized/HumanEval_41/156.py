def car_race_collision(n: int):
    # Initialize two lists to represent the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n, 2 * n)]

    # Iterate through all possible pairs of cars
    for i in range(n):
        for j in range(n):
            # If a left car is equal to a right car, mark it as a collision
            if left_cars[i] == right_cars[j]:
                return 1

    # If no collisions, return 0
    return 0