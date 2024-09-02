

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

    if n <= 1:
        return 0

    race_length = 2 * n
    left_cars = n
    right_cars = n
    left_pos = 0
    right_pos = race_length - 1
    collisions = 0
    while left_cars > 0 and right_cars > 0:
        left_pos += 1
        right_pos -= 1
        if right_pos < left_pos:
            right_pos += race_length
        if right_cars > left_cars:
            right_pos += 1

        if right_pos == left_pos:
            collisions += 1
            right_cars -= 1
            left_cars += 1
    return collisions
