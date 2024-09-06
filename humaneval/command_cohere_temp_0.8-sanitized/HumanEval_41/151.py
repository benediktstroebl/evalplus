def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize the count of collisions
    collision_count = 0

    # Loop until the 2 lists have intersecting elements
    while left_cars[0] != right_cars[n-1] and left_cars[-1] != right_cars[0]:
        # Check if the first car in the left list is equal to the last car in the right list
        if left_cars[0] == right_cars[n-1]:
            collision_count += 1
            left_cars.pop(0)
            right_cars.pop(-1)
        # Alternatively, check if the last car in the left list is equal to the first car in the right list
        elif left_cars[-1] == right_cars[0]:
            collision_count += 1
            left_cars.pop(-1)
            right_cars.pop(0)
        else:
            # If no collisions, shift the left cars by 1 and the right cars by -1
            left_cars = [x+1 for x in left_cars]
            right_cars = [x-1 for x in right_cars]
    
    return collision_count