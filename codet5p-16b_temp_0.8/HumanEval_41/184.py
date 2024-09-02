

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

    left_to_right = [1] + [0] * (n - 1)
    right_to_left = [0] * n + [1]
    for i in range(1, n):
        left_to_right[i] += left_to_right[i - 1] + right_to_left[i - 1]
        right_to_left[n - 1 - i] += left_to_right[n - i] + right_to_left[n - i - 2]
    return sum(left_to_right) - sum(right_to_left)

