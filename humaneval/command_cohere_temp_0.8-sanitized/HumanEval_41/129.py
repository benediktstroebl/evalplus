def car_race_collision(n):
    """
    Determine the number of collisions between two sets of n cars moving in opposite directions.
    """
    if n <= 1:
        return 0

    return n * (n - 1) // 2