

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
    # cars start at 0.5
    cars = {-1: 0.5, 1: 0.5}
    left_cars = 0
    right_cars = 0
    while cars[1] < 1 and cars[-1] < 1:
        # move left cars
        cars[-1] += 0.1
        left_cars += 1
        # move right cars
        cars[1] += 0.1
        right_cars += 1
        # check for collision
        if cars[-1] == cars[1]:
            collisions = 1
            break
    return collisions
