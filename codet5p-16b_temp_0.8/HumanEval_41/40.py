

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

    import sys
    MAX_VAL = sys.maxsize

    def helper(s: int, e: int):
        if s > e:
            return 0

        if s == e:
            return 1

        ret = 0
        for i in range(s, e):
            ret += helper(s, i) * helper(i+1, e)
        return ret

    def helper2(s: int, e: int, left: bool):
        if s > e:
            return 0

        if s == e:
            return 1

        ret = 0
        for i in range(s, e):
            ret += helper2(s, i, not left) * helper2(i+1, e, left)
        return ret

    def helper3(s: int, e: int):
        if s > e:
            return 0

        if s == e:
            return 1

        ret = 0
        for i in range(s, e):
            ret += helper3(s, i) * helper3(i+1, e)
        return ret

    return helper3(
