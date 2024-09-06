def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize collisions counter
    collisions = 0
    
    # Iterate until both lists are equal in length (no more collisions)
    while len(left_cars) != len(right_cars):
        # Find first car on the left list to collide with a car on the right list
        for i in left_cars:
            if i in right_cars[len(right_cars) - 1:]:
                # If a collision occurs, remove it from both lists and increment counter
                collisions += 1
                left_cars.remove(i)
                right_cars.remove(i)
                break
    
    return collisions