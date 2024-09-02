

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
    # make a list of all the cars
    left_list = []
    right_list = []
    for i in range(n):
        left_list.append(i + 1)
        right_list.append(i + 1)

    # make a list of all the cars at the right and left side of the list
    left_side = []
    right_side = []

    for i in range(n):
        left_side.append(left_list[i])
        right_side.append(right_list[-i - 1])

    # make a list of all the pairs
    pairs = []

    for i in range(n):
        pairs.append((left_list[i], right_list[-i - 1]))

    # make a list of all the collisions
    collisions = []

    # check if a collision happened
    for i in range(n):
        if left_side[i] > right_side[i]:
            collisions.append(pairs[i])

    return collisions

