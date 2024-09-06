def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize the collisions counter
    collisions = 0
    
    # Iterate until a car from the left and right lists cross each other's position
    for i in range(n):
        # Find the car on the right moving list that's at the same position as the current left moving car
        right_car_idx = right_cars[i]
        
        while len(right_cars) > right_car_idx:
            if right_cars[right_car_idx] == left_cars[i]:
                collisions += 1
                break
            right_car_idx += 1
        
    return collisions