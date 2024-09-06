def car_race_collision(n: int):
    # Initialize two lists to represent the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n, 2 * n)]

    # Iterate through all possible collisions and count valid collisions between left and right moving cars
    collisions = 0
    for i in range(n):
        if left_cars[i] == right_cars[i]: 
            continue
        elif left_cars[i] > right_cars[i]: 
            left_cars[i] += 1
        else: 
            right_cars[i] += 1
            collisions += 1

    return collisions