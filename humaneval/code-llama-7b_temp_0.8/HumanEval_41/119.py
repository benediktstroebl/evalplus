

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
    n_car_collision = 0
    i = 0
    j = 0

    while i < n:
        if j == n:
            j = 0
        if i == n:
            break

        if i > j:
            j += 1
        elif i < j:
            i += 1
        else:
            n_car_collision += 1
            i += 1
            j += 1

    return n_car_collision

