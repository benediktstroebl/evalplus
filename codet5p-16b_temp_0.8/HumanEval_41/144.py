

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

    assert n > 0
    if n <= 2:
        return 0

    time_step = 1
    left_to_right = [0]*n
    right_to_left = [0]*n

    for i in range(n):
        left_to_right[i] = time_step
        time_step += 1

    for i in range(n-1, -1, -1):
        right_to_left[i] = time_step
        time_step += 1

    collisions = 0
    for i in range(n):
        if right_to_left[i] <= left_to_right[i]:
            collisions += 1

    return collisions

