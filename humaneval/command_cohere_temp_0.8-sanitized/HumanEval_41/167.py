import math
def car_race_collision(n: int) -> int:
    """
    Count the number of collisions between infinitely strong cars moving in opposite directions on an infinitely long straight road.
    """
    # Calculate the number of cars in each group
    left_cars = n // 2
    right_cars = n - left_cars
    
    # Determine possible collision points
    collisions = (right_cars + left_cars - 1) // 2
    
    # Ensure proper counting
    if right_cars >= left_cars:
        return collisions
    else:
        return math.inf