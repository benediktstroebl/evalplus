

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
    l_to_r_cars = [i+1 for i in range(n)]
    r_to_l_cars = [i+1 for i in range(n-1, -1, -1)]

    collisions = 0
    i = 0
    while i < n:
        collisions += l_to_r_cars[i] * r_to_l_cars[n-i-1]
        i += 1
    return collisions

