def car_race_collision(n):
    num_collisions = 0
    for i in range(n):
        for j in range(n):
            if i != j and (i + j) % 2 == 0:
                num_collisions += 1
    return num_collisions