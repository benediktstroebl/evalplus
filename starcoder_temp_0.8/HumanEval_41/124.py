

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
    right_to_left = [i for i in range(n)]
    left_to_right = [i for i in range(n)]
    collisions = 0
    while len(right_to_left) > 0 and len(left_to_right) > 0:
        if right_to_left[0] >= len(left_to_right):
            collisions += len(right_to_left)
            right_to_left = right_to_left[1:]
        elif left_to_right[0] >= len(right_to_left):
            collisions += len(left_to_right)
            left_to_right = left_to_right[1:]
        elif right_to_left[0] < left_to_right[0]:
            collisions += 1
            right_to_left = right_to_left[1:]
        else:
            collisions += 1
            left_to_right = left_to_right[1:]
    return collisions
