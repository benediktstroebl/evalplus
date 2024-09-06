

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
    # n = 100
    c1 = 0
    c2 = 0
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                if j % 2 != 0:
                    c1 += 1
        else:
            for j in range(n-1, -1, -1):
                if j % 2 != 0:
                    c2 += 1
    return c1 + c2

