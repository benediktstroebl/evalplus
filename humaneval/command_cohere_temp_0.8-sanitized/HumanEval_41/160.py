def car_race_collision(n):
    cars_left = n // 2
    cars_right = n - cars_left
    collisions = 0

    for i in range(cars_left):
        for j in range(cars_right):
            if i == j:
                continue
            elif i + j >= n:
                collisions += 1
            else:
                collisions += 2 * (i + 1) * (j + 1)
    return collisions