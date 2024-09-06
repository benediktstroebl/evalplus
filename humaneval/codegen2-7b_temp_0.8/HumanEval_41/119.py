

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
    num_collisions = 0
    for _ in range(n):
        idx_left = (idx_left + 1) % n
        idx_right = (idx_right + 1) % n
        if (cars[idx_left].distance_to(cars[idx_right]) <=
            cars[idx_left].speed):
            num_collisions += 1

    return num_coll
