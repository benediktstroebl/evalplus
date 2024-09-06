def car_race_collision(n):
    cars_1 = n // 2
    cars_2 = n - cars_1
    collisions = 0

    for i in range(cars_1):
        for j in range(cars_2):
            if i + j >= n:
                collisions += 1
    return collisions