def car_race_collision(n: int):
    # Define two lists to store the positions of left and right driving cars.
    left_driving = [i for i in range(n)]
    right_driving = [i for i in range(n, 2 * n)]

    # Find intersections between the two lists. These are the colliding cars.
    collisions = list(set(left_driving) & set(right_driving))

    # If there are no collisions, return 0.
    if not collisions:
        return 0
    
    # If there are collisions, return the number of collisions.
    return len(collisions)