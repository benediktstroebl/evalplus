

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

    collisions = 0
    left_to_right = list(range(1, n + 1))
    right_to_left = list(range(n, 0, -1))
    for car_1 in left_to_right:
        for car_2 in right_to_left:
            if car_1 == car_2:
                collisions += 1
    return collisions
