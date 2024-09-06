def car_race_collision(n: int):
    # Initialize two lists to represent the positions of cars moving left to right and right to left.
    left_to_right = [i for i in range(n)]
    right_to_left = [i for i in range(n)]
    
    # Initialize collision variable to track collisions.
    collisions = 0
    
    # Iterate through all combinations of cars from the two lists.
    for i in range(n):
        # For each car moving left to right, check if there's a car moving right to left at the same position.
        if left_to_right[i] == right_to_left[i]:
            # If a match is found, increment the collisions variable.
            collisions += 1
        
        # Since the cars are infinitely sturdy, we can update their positions as if no collision occurred.
        # Move each car in both lists to the next position.
        left_to_right[i] += 1
        right_to_left[i] += 1

    return collisions