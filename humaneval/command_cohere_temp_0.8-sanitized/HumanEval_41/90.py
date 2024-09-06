def car_race_collision(n: int):
    """
    Determine the number of collisions when two sets of n cars
    simultaneously move in opposite directions on an infinitely long straight road.
    """
    dir1, dir2 = -1, 1
    car_position = [i for i in range(n)]
    
    # Initialize a counter for collisions
    collision_count = 0
    
    # Set a flag to determine direction of second-to-last car
    is_last_car = False
    
    while True:
        # Update car positions for current direction
        for i in range(n):
            car_position[i] += dir1 if not is_last_car else dir2
        
        # Find cars that collide
        for i in range(n):
            if car_position[i] > 0 and car_position[i] - 1 < n:
                collision_count += 1
                car_position[i] = -1  # Move collided car out of the way
        
        # Switch direction for next iteration
        dir1, dir2 = dir2, dir1
        
        # Break the loop if all cars have collided or are removed
        if all(car_position == -1) or all(car_position >= n) or is_last_car:
            break
        
        is_last_car = not is_last_car
    
    return collision_count