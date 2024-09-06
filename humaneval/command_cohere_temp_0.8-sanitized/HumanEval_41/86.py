def car_race_collision(n: int):
    """
    Determine the number of collisions when two sets of n cars moving in opposite directions 
    along an infinitely long straight road collide.
    
    Parameters:
        n (int): Number of cars in each set.

    Returns:
        int: Number of collisions between the moving cars.
    """
    if n <= 1:
        return 0
    
    collisions = 0
    car_interval = n - 1    # Interval between cars in one set.
    total_cars = 2 * n - 1  # Total cars on the road.

    # Calculate the number of collisions when cars are moving halfway between their positions.
    halfway_move = (car_interval // 2) + (car_interval // 3)
    collisions += total_cars // 2 - (halfway_move // 2)

    return collisions