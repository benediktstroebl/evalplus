def car_race_collision(n: int):
    # Initialize two lists to keep track of cars on the left and right lanes
    cars_left = []
    cars_right = []

    # Simulate the movement of cars in both directions
    for _ in range(n): 
        # For each car, determine the index at which it would collide with a car in the other lane
        collision_idx = len(cars_right) - (len(cars_left) + 1)
        cars_left.append(collision_idx)
        cars_right.append(len(cars_right))
    
    # Determine the number of collisions by comparing car indices in both lanes
    collision_count = sum(abs(x - y) < 1 for x, y in zip(cars_left, cars_right))
    
    return collision_count