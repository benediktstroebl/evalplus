def car_race_collision(n):
    # Define 2 lists to hold the cars from each direction
    cars_right_left = []
    cars_left_right = []
    
    # Initialize cars in each list
    for _ in range(n):
        cars_right_left.append(1)
        cars_left_right.append(-1)
    
    # Set up trackers for car collisions
    collisions_right_left = 0
    collisions_left_right = 0
    
    # Iterate through pairs of cars to check for collisions
    for i in range(n-1):
        if cars_right_left[i] == cars_right_left[i+1] and cars_right_left[i] == -cars_left_right[i]:
            collisions_right_left += 1
        if cars_left_right[i] == cars_left_right[i+1] and cars_left_right[i] == -cars_right_left[i]:
            collisions_left_right += 1
    
    return collisions_right_left + collisions_left_right