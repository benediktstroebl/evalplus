def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize collisions as 0
    collisions = 0
    
    # Move left cars to the right
    for i in range(n):
        left_cars[i] += 1
        
        # Check for collisions with right-moving cars
        for j in range(n):
            if left_cars[i] == right_cars[j] and i != j:
                collisions += 1
    
    # Move right cars to the left
    for i in range(n):
        right_cars[i] -= 1
        
        # Check for collisions with left-moving cars
        for j in range(n):
            if right_cars[i] == left_cars[j] and i != j:
                collisions += 1
    
    return collisions