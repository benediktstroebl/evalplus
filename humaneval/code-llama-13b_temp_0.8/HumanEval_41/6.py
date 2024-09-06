

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

    left_to_right = [0] * n
    right_to_left = [n - 1] * n
    left_to_right_idx, right_to_left_idx = 0, 0
    collisions = 0
    while left_to_right_idx < n:
        left_to_right_idx += 1
        if left_to_right[left_to_right_idx] < right_to_left[right_to_left_idx]:
            right_to_left_idx += 1
        else:
            collisions += 1
    return collisions


