def car_race_collision(n: int):
    # Initialize two lists to represent the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize collision tracking variable
    collisions = 0
    
    # Iterate until both lists are equal in length (no more collisions)
    while len(left_cars) > len(right_cars) or len(right_cars) > len(left_cars):
        # Find the car on the left that's not in the right list or vice-versa
        left_car = left_cars.pop() if len(left_cars) > len(right_cars) else right_cars.pop()
        right_car = right_cars.pop() if len(right_cars) > len(left_cars) else left_cars.pop()
        
        # If cars are moving in the same direction, ignore
        if left_car == right_car:
            continue
        
        # If cars collide, increment collision count
        collisions += 1
        
        # Insert the moved cars into their respective opposite lists
        left_cars.append(left_car)
        right_cars.append(right_car)
    
    return collisions