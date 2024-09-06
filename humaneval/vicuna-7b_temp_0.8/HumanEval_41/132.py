

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
    if n < 1:
        return 0
    if n == 1:
        return 1

    for i in range(1, n):
        for j in range(1, n):
            if i != j and (i + j) % 2 == 0:
                # two cars at the same position
                return 1
        # all cars except one at the rightmost position
        # are moving left to right
        # and collisions between cars moving left to right are impossible
        return 1

    # all remaining cases are collisions between cars moving right to left
    return n - 1