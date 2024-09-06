def car_race_collision(n: int):
    # Initialize two lists to represent the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize collision tracking variables
    collisions = 0
    min_left, max_right = 0, n - 1
    
    while min_left <= max_right:
        # Identify cars that are moving in different directions and count collisions
        if left_cars[min_left] <= right_cars[max_right]:
            collisions += max_right - min_left + 1
            max_right -= 1
        else:
            min_left += 1
    
    return collisions