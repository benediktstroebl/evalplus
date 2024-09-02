

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
    collisions = 0
    l2r = [0] * n
    r2l = [n-1] * n
    while l2r[0] < r2l[0]:
        for i in range(n):
            if l2r[i] < r2l[i]:
                l2r[i] += 1
            else:
                r2l[i] -= 1
            if l2r[i] == r2l[i]:
                collisions += 1
    return collisions

