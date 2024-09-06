

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

    # The number of collisions can be computed by the following recurrence relation.
    # F(n) = F(n-1) + n, with F(0) = 0, where n is the number of cars on the road.
    # This is similar to the Fibonacci sequence, and the closed form of the recurrence
    # relation is F(n) = F(n-1) + n - 1.
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1

    F = [0] * (n + 1)
    F[0] = 0
    F[1] = 0
    F[2] = 1
    for i in range(3, n + 1):
        F[i] = F[i - 1] + i - 1
    return F[n]


