def car_race_collision(n: int):
    """
    Determine the number of collisions when two sets of n cars move towards each other on an infinitely long straight road.

    Args:
        n (int): Number of cars in each set.

    Returns:
        int: Number of collisions between the moving cars.
    """

    # Calculate the number of collisions when moving cars are aligned.
    collisions = n - 1

    # When cars are moving in the same direction, they overlap completely.
    if n % 2 == 0:
        collisions //= 2

    return collisions