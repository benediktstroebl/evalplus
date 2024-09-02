

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
    total = 0
    # set distance of cars in two directions
    left_to_right = [0] * n
    right_to_left = [0] * n
    # each car starts at distance zero
    left_to_right[0] = 0
    right_to_left[0] = 0
    # with time t, the distances are
    for t in range(1, 2*n):
        # find index of car moving left to right
        ind = min(range(n), key=lambda i: left_to_right[i])
        left_to_right[ind] += t
        # find index of car moving right to left
        ind = min(range(n), key=lambda i: right_to_left[i])
        right_to_left[ind] += t
        # if cars are already closer than distance, count collision
        if left_to_right[ind] - right_to_left[ind] == 0:
            total += 1
    return total

