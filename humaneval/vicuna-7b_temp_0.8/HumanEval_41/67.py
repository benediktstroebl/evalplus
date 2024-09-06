

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
    # sort the cars by their speed
    cars = sorted(range(n), key=lambda x: x // 10)
    
    # initialize the number of collisions
    collisions = 0
    
    # check for the first car
    for i in range(1, len(cars)):
        if cars[i] < cars[i-1] and cars[i] < cars[i-1] * 3 / 4:
            collisions += 1
    
    # check for the rest of the cars
    for i in range(1, len(cars)):
        if cars[i] > cars[i-1] * 3 / 4:
            collisions += 1
    
    return collisions