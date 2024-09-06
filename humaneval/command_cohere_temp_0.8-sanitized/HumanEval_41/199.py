def car_race_collision(n: int):
    # Initialize two lists to represent the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize collision tracking variable
    collisions = 0
    
    # Iterate until both lists are equal in length (no more collisions)
    while len(left_cars) != len(right_cars):
        # Find first index of difference between left_cars and right_cars
        # If the first index is beyond the current length, move to the next step
        first_diff = left_cars[0] if len(left_cars) <= len(right_cars) else right_cars[0]
        
        for car in left_cars:
            if car != first_diff and right_cars[car] == car:
                # If there's a match, increment the collision count and remove the collided car from both lists
                collisions += 1
                left_cars.remove(car)
                right_cars.remove(car)
                break
        
        # Shuffle right_cars to the beginning of left_cars to simulate motion
        left_cars = right_cars + left_cars
        right_cars = []
    
    return collisions