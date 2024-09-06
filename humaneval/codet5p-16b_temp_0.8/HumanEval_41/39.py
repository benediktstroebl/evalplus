

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
    left = right = 0
    left_count = 0
    right_count = 0
    for i in range(2 * n):
        left_new = max(left - 1, 0)
        right_new = right + 1
        left = left_new
        right = right_new
        if left == right:
            left_count += 1
        if right == n + left:
            right_count += 1
    return left_count + right_count


