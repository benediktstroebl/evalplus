def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize collisions counter
    collisions = 0

    # Move left cars to the right and right cars to the left
    for _ in range(n):
        # Find the furthest left right-moving car and the furthest right left-moving car
        left_idx = right_cars.index(-1)
        right_idx = left_cars.index(n - 1)
        
        # If they are not the same, there was a collision
        if left_idx != right_idx:
            collisions += 1
        
        # Move the right car out of the way
        right_cars[right_idx] = right_cars[right_idx] - 1
        # Move the left car ahead
        left_cars[left_idx] = left_cars[left_idx] + 1

    return collisions