def car_race_collision(n):
    # Define two lists to represent the positions of cars moving left to right and right to left.
    ltr_positions = [i for i in range(n)]
    rtl_positions = [i for i in range(n)]
    
    collision_count = 0
    
    # Loop until the two lists have overlapping elements.
    while ltr_positions and rtl_positions:
        # Find the car in the left-to-right list with the smallest position.
        min_ltr_pos = min(ltr_positions)
        ltr_positions.remove(min_ltr_pos)
        
        # Find the car in the right-to-left list with the largest position.
        max_rtl_pos = max(rtl_positions)
        rtl_positions.remove(max_rtl_pos)
        
        # If the two cars collided, increment the collision count.
        if min_ltr_pos == max_rtl_pos:
            collision_count += 1
    
    return collision_count