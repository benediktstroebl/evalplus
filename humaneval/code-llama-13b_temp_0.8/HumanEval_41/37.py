

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

    if n == 0:
        return 0

    # The function is symmetric.  If we can find the number of collisions in the case n,
    # then the number of collisions in the case n+1 is the same, except that we need
    # to add an extra car on the right to right direction, so we have an extra collision.
    return car_race_collision(n-1) + 1



