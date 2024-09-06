def car_race_collision(n: int):
    # Initialize two lists to keep track of cars moving left to right and right to left
    cars_left_right = [False] * n
    cars_right_left = [False] * n

    # Toggle the state of cars when they "collide"
    for i in range(1, n):
        if cars_left_right[i - 1] and not cars_right_left[i]:
            cars_left_right[i] = True
            cars_right_left[i] = True

    # Count the number of "collisions"
    collision_count = sum(1 for i in range(n - 1) if cars_left_right[i] and cars_right_left[i])

    return collision_count