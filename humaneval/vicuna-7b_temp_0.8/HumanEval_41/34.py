

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
    # your code here

    # Using binary search to solve the problem
    collision_count = 0
    left_to_right_start = 0
    left_to_right_end = n - 1
    right_to_left_start = n - 1
    right_to_left_end = 0

    while left_to_right_start < left_to_right_end and \
           right_to_left_start < right_to_left_end:
        mid = (left_to_right_start + right_to_left_start) // 2
        if mid == 0:
            # no collision
            continue
        else:
            # collide
            collision_count += 1
            mid -= 1

        # check for left-to-right collision
        left_to_right_start = mid + 1
        while left_to_right_start < left_to_right_end and \
               right_to_left_start < right_to_left_end and \
               left_to_right_start - mid >= 1:
            # no collision
            left_to_right_start += 1
        if left_to_right_start == left_to_right_end:
            # all left-to-right cars passed by this point
            collision_count += 1

        # check for right-to-left collision
        right_to_left_start = mid - 1
        while right_to_left_start >= right_to_left_end and \
               left_to_right_start < left_to_right_end and \
               right_to_left_start + mid - 1 <= n - 1:
            # no collision
            right_to_left_start -= 1
        if right_to_left_start == right_to_left_end:
            # all right-to-left cars passed by this point
            collision_count += 1

        # adjust range of search
        if left_to_right_start > mid:
            left_to_right_start = mid
        if right_to_left_start < mid:
            right_to_left_
