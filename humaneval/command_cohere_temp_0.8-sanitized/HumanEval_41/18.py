def car_race_collision(n: int):
    # Initialize two lists to represent the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n, 2 * n)]

    # Loop to find collisions between the two lists of cars
    collisions = 0
    for i in range(n - 1):
        if left_cars[i] == right_cars[i]:
            collisions += 1
        # Move the right-moving cars to the right by incrementing their positions
        right_cars[i + 1] = right_cars[i] + 1

    return collisions