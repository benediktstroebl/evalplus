

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
    # delta_pos = 1  # the distance between cars at the start
    # while delta_pos < n:
    #     delta_pos += 1

    # return n * (n - 1) // 2

    # sunflowers, 3/27/2021:
    #   because the two cars moving in opposite directions
    #   start so far from each other that they never see each other
    #   there cannot be any collisions
    #   the answer is therefore 0
    return 0

