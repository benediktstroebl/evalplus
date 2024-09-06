

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

    # this is the method you are required to implement.
    # you may NOT change any of the code provided above.

    collisions = 0
    for left_to_right_car in range(n):
        for right_to_left_car in range(n):
            if left_to_right_car == right_to_left_car:
                continue
            if left_to_right_car > right_to_left_car:
                if left_to_right_car - right_to_left_car <= n - 1:
                    collisions += 1
    return collisions
