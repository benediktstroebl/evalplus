

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

    assert n >= 1, f"n must be at least 1; got {n}"
    from math import ceil, floor
    cars_left = ceil(n / 2)
    cars_right = n - cars_left
    collisions = 0
    cars_left_in_lane = 0
    cars_right_in_lane = 0
    for i in range(n):
        if i % 2 == 0:
            cars_left_in_lane += 1
            cars_left -= 1
        else:
            cars_right_in_lane += 1
            cars_right -= 1
        if cars_left_in_lane == cars_left and cars_right_in_lane == cars_right:
            collisions += 1
    return collisions

