def car_race_collision(n: int):
    collisions = 0
    for i in range(n):
        for j in range(n):
            if i != j and (i + j) % 2 == 0:
                collisions += 1
    return collisions