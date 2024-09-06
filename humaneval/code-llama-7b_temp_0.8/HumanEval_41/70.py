

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
    assert n >= 0
    if n <= 1:
        return 0

    # the number of collisions
    c = 0

    # the number of cars that are already passed
    n_past = 0

    # the number of cars that will be past
    n_past_next = 0

    while n_past < n:

        # the number of cars that are ahead
        n_ahead = n - n_past

        # the number of cars that will be ahead
        n_ahead_next = n - n_past_next

        # the number of collisions in this round
        c += n_past * n_ahead_next

        # add the number of cars that are ahead to the ones that will be past
        n_past_next += n_ahead

        # add the number of cars that will be past to the ones that will be past next round
        n_past_next += n_ahead_next

        # move the ones that will be past to the beginning
        n_past = n_past_next

        # reset the number of cars that will be past to zero
        n_past_next = 0

    return c

