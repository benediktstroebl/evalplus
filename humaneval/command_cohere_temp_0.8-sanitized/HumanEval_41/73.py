def car_race_collision(n):
    """
    Determine the number of collisions when two sets of n cars each move in opposite directions 
    along an infinitely long, straight road and assume that all cars move at the same speed.
    """
    # Define variables for tracking positions and velocities for cars moving right to left
    right_left_cars = [(0, 1) for _ in range(n)]
    
    # Initialize a variable to track the number of collisions
    collision_count = 0

    # Iterate through the right-left cars to detect collisions with the left-right cars
    for i in range(n):
        for j in range(n):
            # Calculate the current positions of the cars
            right_pos = right_left_cars[i][0]
            left_pos = -1 * left_right_cars[j][0]
            
            # Determine if a collision has occurred if the cars have met
            if right_pos > left_pos:
                collision_count += 1
    
    return collision_count