def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize collisions counter
    collisions = 0
    
    # Move left cars to the right
    for i in range(n):
        left_cars[i] += 1
        # Check if any left car collided with a right car
        if left_cars[i] == right_cars[i]:
            collisions += 1
        # If not, move the left car but no collision
        else:
            left_cars[i] = 0
    
    # Move right cars to the left
    for i in range(n):
        right_cars[i] -= 1
        # Check if any right car collided with a left car
        if right_cars[i] == left_cars[i]:
            collisions += 1
        # If not, move the right car but no collision
        else:
            right_cars[i] = 0
    
    return collisions