def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right driving cars.
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize collisions as 0.
    collisions = 0

    # Move left cars to the right.
    for i in range(n):
        left_cars[i] += 1
        
        # Check for collisions.
        for j in range(n):
            if left_cars[i] == right_cars[j] and left_cars[i] != right_cars[j] - 1:
                collisions += 1
                break
        
        # Update right_cars.
        right_cars[j] += 1
    
    return collisions