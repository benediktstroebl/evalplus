

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

    def n_collisions(ns: list):
        collisions = 0
        for i in range(len(ns)-1):
            if ns[i] == 1 and ns[i+1] == 2:
                collisions += 1
        return collisions

    if n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        ns = [0] * (n + 1)
        ns[0] = 1
        ns[n] = 2
        return n_collisions(ns)

