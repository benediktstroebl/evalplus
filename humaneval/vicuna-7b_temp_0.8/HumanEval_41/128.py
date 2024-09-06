

def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """

    # Initialize variables for the cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]

    # Sort the left and right cars by their index
    left_cars.sort()
    right_cars.sort()

    # Initialize variables for the collision counts
    collision_count_left = 0
    collision_count_right = 0

    # Iterate through the left cars
    for i in range(n):
        # If the current left car is less than the middle of the right cars, there
        # is no collision and the count remains zero
        if i < (n // 2):
            continue
        # If the current right car is less than the middle of the left cars, there
        # is no collision and the count remains zero
        if i < (n // 2):
            continue
        # If the current left car is equal to the middle of the right cars, the
        # collision count remains zero because both sets of cars passed each other
        if i == (n // 2):
            continue
        # If the current right car is equal to the middle of the left cars, the
        # collision count remains zero because the two sets of cars passed each other
        if i == (n // 2):
            continue
        # Otherwise, a collision occurs and the count is incremented by one
        collision_count_left += 1
        collision_count_right += 1
    # Return the sum of the collision counts
    return collision_count_left + collision_count_right
