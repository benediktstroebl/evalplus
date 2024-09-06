def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right driving cars.
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize collisions as 0.
    collisions = 0
    
    # Move left cars to the right and right cars to the left until collision.
    while len(left_cars) > 0 and len(right_cars) > 0:
        # Find the car from each list closest to the other list and swap.
        i = min([(car - j) ** 2 for i, car in enumerate(left_cars) for j in right_cars])
        j = min([(car - i) ** 2 for j, car in enumerate(right_cars) for i in left_cars])
        
        # Decrement the number of cars on the lists.
        left_cars.remove(i)
        right_cars.remove(j)
        
        # Increment collision if cars swapped.
        collisions += (i < j)
        
        # Move to next pair of cars.
    return collisions