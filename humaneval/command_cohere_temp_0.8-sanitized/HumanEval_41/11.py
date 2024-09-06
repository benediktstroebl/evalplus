def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize the collision variable to 0
    collisions = 0
    
    # Loop until the 2 lists have overlapping cars
    while len(set(left_cars) & set(right_cars)):
        # Find the first index of a car moving from left to right in the right_cars list
        right_collisions = right_cars.index(min(right_cars), len(left_cars)-1) + 1
        # Find the first index of a car moving from right to left in the left_cars list
        left_collisions = left_cars.index(min(left_cars) + n, len(left_cars))
        
        # Update the number of collisions and reset the lists where collisions occur
        collisions += (right_collisions - left_collisions) / 2
        left_cars[left_collisions:right_collisions] = []
        right_cars[right_collisions:left_collisions] = []
    
    return collisions