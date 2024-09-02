

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

    def check(s):
        return len(s) == len(set(s))

    if n == 1:
        return 0

    def check(s):
        return len(s) == len(set(s))

    a, b = ['l'] * n, ['r'] * n
    for i in range(1, n):
        for j in range(n):
            if j + i < n:
                a[j + i] = 'l'
            if j - i >= 0:
                b[j - i] = 'r'
            if check(a) and check(b):
                return 1

    return 0
