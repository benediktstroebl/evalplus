def car_race_collision(n):
    cars_left = n // 2
    cars_right = n - cars_left
    collisions = 0

    for i in range(cars_left):
        for j in range(cars_right):
            if i + j > cars_left + cars_right - 1:
                continue
            collisions += 1
    return collisions