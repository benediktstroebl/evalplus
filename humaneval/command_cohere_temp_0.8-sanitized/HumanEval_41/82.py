def car_race_collision(n: int):
    from itertools import zip_longest

    cars_1 = [i for i in range(n)]
    cars_2 = [i for i in range(n)]
    zipped = zip_longest(cars_1, cars_2, fillvalue=0)
    collisions = sum(1 for a, b in zipped if a == b)
    return collisions