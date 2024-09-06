def car_race_collision(n: int):
    # Initialize two lists to represent the positions of left and right driving cars.
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize a variable to track collisions.
    collisions = 0
    
    # Iterate through the cars in both lists.
    for i in range(n):
        # If a car is in both lists, they collide.
        if left_cars[i] in right_cars and right_cars[i] in left_cars:
            collisions += 1
            # Remove collisions to prevent double-counting.
            left_cars.remove(right_cars[i])
            right_cars.remove(left_cars[i])
    
    return collisions