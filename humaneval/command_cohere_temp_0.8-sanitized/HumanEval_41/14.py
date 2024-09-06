def car_race_collision(n: int):
    # Calculate the number of collisions when moving cars meet
    collisions = n * (n - 1) // 2

    return collisions