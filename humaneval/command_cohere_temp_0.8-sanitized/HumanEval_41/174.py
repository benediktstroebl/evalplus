def car_race_collision(n: int):
    # Define two lists to store the positions of left and right driving cars.
    left_driving = [i for i in range(n)]
    right_driving = [i for i in range(n, 2 * n)]

    # Find collisions between cars driving from left to right and right to left.
    collisions = set(left_driving) & set(right_driving)
    
    # Return the number of collisions.
    return len(collisions)