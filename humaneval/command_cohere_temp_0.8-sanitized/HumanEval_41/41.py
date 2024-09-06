def car_race_collision(n: int):
    # Initialize two lists to keep track of cars moving left to right and right to left
    moving_right = [False] * n
    moving_left = [False] * n
    
    # Toggle the movement of every second car
    for i in range(1, n, 2):
        moving_right[i] = True
    
    for i in range(0, n - 1, 2):
        moving_left[i] = True
    
    # Count the number of collisions
    collisions = sum(1 for i in range(n) if moving_right[i] and moving_left[i])
    
    return collisions