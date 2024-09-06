

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

    # we start at the 1st index and count the numbers until we reach the last index
    # for both arrays.  When we reach the last index, we go back to the start of the
    # array.

    collisions = 0
    left_to_right = 0
    right_to_left = 0

    for index in range(0, 2*n-1):
        left_to_right = left_to_right + 1
        right_to_left = right_to_left + 1
        collisions = collisions + max(left_to_right, right_to_left)

        if index == 2*n-2:
            left_to_right = 0
            right_to_left = 0

    return collisions

