

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

    assert n > 0

    cache = dict()
    def a_race(n: int):
        if n < 0:
            return 0
        if n == 0:
            return 1

        if (n, n) not in cache:
            cache[(n, n)] = a_race(n - 2) + a_race(n - 1)

        return cache[(n, n)]

    return a_race(n) - 1
