

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
    x = [0]*n
    x[0] = 0
    for i in range(1,n):
        x[i] = x[i-1]+1

    y = [0]*n
    y[n-1] = 0
    for i in range(n-2,-1,-1):
        y[i] = y[i+1]+1
    y = y[::-1]
    c = 0
    for i in range(n-1):
        c+= x[i] * y[i+1]
    return c

