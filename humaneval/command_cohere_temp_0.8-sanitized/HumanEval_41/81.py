def car_race_collision(n: int):
    from itertools import zip_longest

    cars_left = list(range(n))
    cars_right = list(range(n))

    collisions = 0

    for left_car, right_car in zip_longest(cars_left, cars_right, fillvalue=None):
        if left_car == right_car:
            collisions += 1

    return collisions