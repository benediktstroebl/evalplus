def car_race_collision(n: int):
    # Define two lists to store car positions for each group
    l1, l2 = [], []
    
    # Define a sentinel value to act as a boundary for car positions
    sentinel = float('-inf') * n

    # Iterate through both lists to check for collisions
    for car_1 in range(n):
        for car_2 in range(n):
            # If the two cars are the same or a collision occurs, skip iteration
            if car_1 == car_2 or l1[car_1] == l2[car_2]:
                continue
            # If cars don't move past each other, mark them as colliding
            elif l1[car_1] <= l2[car_2] <= sentinel or l2[car_2] <= l1[car_1] <= sentinel:
                return 1
    
    # If no collisions occur, return 0
    return 0