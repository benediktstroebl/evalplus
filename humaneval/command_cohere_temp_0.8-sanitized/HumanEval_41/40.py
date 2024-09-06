def car_race_collision(n: int):
    # Define the two sets of cars as two lists
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n, 2 * n)]
    
    # Count collisions when cars are moving towards each other
    collisions = sum(1 for l in left_cars if l in right_cars)
    
    # Remove the doubled car and return the number of collisions
    return collisions - max(collisions / 2, 1)