

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

    print(n)
    if n == 1:
        return 1

    l = [None] * n
    r = [None] * n

    l[0] = r[-1] = 1
    l[1] = r[-2] = 2

    for i in range(2, n):
        l[i] = r[i-2] = l[i-1] + r[i-1]
    return sum(l)

