

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
    left_to_right = [1] * n
    right_to_left = [1] * n
    right_to_left.reverse()
    total_collisions = 0

    while True:
        next_left_to_right = [1] * n
        next_right_to_left = [1] * n
        next_right_to_left.reverse()

        for i in range(n):
            next_left_to_right[i] = max(0, left_to_right[i] + right_to_left[i])
            next_right_to_left[i] = max(0, right_to_left[i] + left_to_right[i])

        total_collisions += next_left_to_right[0] + next_right_to_left[0]

        if next_left_to_right == left_to_right and next_right_to_left == right_to_left:
            return total_collisions

        left_to_right = next_left_to_right
        right_to_left = next_right_to_left

