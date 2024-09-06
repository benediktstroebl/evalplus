def car_race_collision(n: int):
    """
    Determine the number of collisions when two sets of n cars move towards each other on an infinitely long straight road.
    """
    # Define variables for the number of cars moving from the left and right directions
    cars_left = 2 * n - 1
    cars_right = n - 1

    # Calculate the number of collisions when n is equal to 1, 2, and 3 to derive the pattern
    if n == 1:
        return 0
    elif n == 2:
        return cars_left
    elif n == 3:
        return cars_left + cars_right
    # Define the dynamic formula for any n
    else:
        return cars_left + cars_right - n