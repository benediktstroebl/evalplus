def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right driving cars.
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize collisions as 0.
    collisions = 0

    # Move both lists of cars towards each other by subtracting 1 from the left list and adding 1 to the right list.
    left_cars = [i-1 for i in left_cars]
    right_cars = [i+1 for i in right_cars]
    
    # Compare both lists to find collisions.
    collisions_curr = left_cars[:len(left_cars) - len(right_cars)]
    collisions += len(collisions_curr)
    
    # Return the final collision count.
    return collisions