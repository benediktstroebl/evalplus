def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right driving cars.
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize collisions as 0.
    collisions = 0
    
    # Move left cars to the right and right cars to the left until collision.
    while len(left_cars) > 0 and len(right_cars) > 0:
        # Remove the first left car and add to the right list.
        right_cars.append(left_cars.pop(0))
        # Remove the last right car and add to the left list.
        left_cars.append(right_cars.pop())
        
        # Increment collision count if the car was moved from left to right.
        collisions += left_cars.index(right_cars.pop())
    
    return collisions