

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
    from math import log
    A, B = 1, 1
    N = 2 ** n - 1
    S = (1 / (n + 1)) * (A * B / (N + 1))
    while abs(log(S, 2) - (n + 1)) > 0.00001:
        A, B = A + 1, B + 2
        N += 2
        S = (1 / (n + 1)) * (A * B / (N + 1))
    return N

