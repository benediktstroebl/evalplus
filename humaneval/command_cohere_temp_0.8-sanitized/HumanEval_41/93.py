def car_race_collision(n: int):
    """
    Determine the number of collisions when two sets of n cars move towards each other on an infinitely long straight road.
    """
    # Define variables for the number of cars moving from left to right and right to left.
    left_to_right = 2 * n - 1

    # Use the formula to calculate the number of collisions.
    collisions = (left_to_right + 1) // 2

    # Return the number of collisions.
    return collisions