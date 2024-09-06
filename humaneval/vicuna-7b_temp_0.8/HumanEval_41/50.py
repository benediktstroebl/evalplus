

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
    # your code here
    i, j = 0, 0
    while i < n and j < n:
        if i == n - 1 and j == 0 or i == 0 and j == n - 1:
            return 1
        elif (i + 1 == n or i - 1 == n) and (j + 1 == n or j - 1 == n):
            return 1
        i += 1
        j += 1
    return 0