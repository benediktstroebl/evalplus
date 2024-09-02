

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
    # assert n > 1
    n = int(n)
    # n = n if n > 1 else 1
    # n = n if n > 1 else 1
    # n = int(n)
    # n = int(n) if n > 1 else 1
    if n <= 1:
        return 0
    n = int(n)
    # n = n if n > 1 else 1
    # n = int(n)
    # n = int(n) if n > 1 else 1
    # n = int(n)
    if n == 1:
        return 0
    # if n == 1:
    #     return 0
    # if n == 2:
    #     return 1
    # if n == 3:
    #     return 2
    # if n == 4:
    #     return 3
    # if n == 5:
    #     return 4
    # if n == 6:
    #     return 6
