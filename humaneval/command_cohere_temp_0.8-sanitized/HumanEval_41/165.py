def car_race_collision(n: int):
    # Initialize two lists to hold the positions of left and right driving cars
    left_drive = [i for i in range(n)]
    right_drive = [i for i in range(n)]
    
    # Initialize collision tracking variable
    collisions = 0
    
    # Iterate until both lists are equal in length (no more collisions)
    while len(left_drive) > len(right_drive) or len(right_drive) > len(left_drive):
        # Find the car indices that are driving on each side
        left_idx, right_idx = 0, 0
        
        # Iterate to find the next car indices driving on each side
        while left_idx < len(left_drive) and right_idx < len(right_drive):
            # Calculate the distance between the cars (absolute difference)
            distance = abs(left_drive[left_idx] - right_drive[right_idx])
            
            # Increment the index for the next car driving on the left
            left_idx += 1
            
            # Increment the index for the next car driving on the right
            right_idx += 1
            
            # If the distance is less than or equal to 1, a collision occurs
            if distance <= 1:
                collisions += 1
                
                # Remove the collided cars from both lists
                left_drive.remove(left_drive[left_idx-1])
                right_drive.remove(right_drive[right_idx-1])
                
                # Ensure the removed cars are not accounted for in the loop below
                left_idx -= 1
                right_idx -= 1
    
    return collisions