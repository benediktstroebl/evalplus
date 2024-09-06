

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

    # find the number of collisions assuming n cars are driving left to right;
    # simultaneously, another set of n cars are driving right to left.
    # The two sets of cars start out being very far from each other.
    n_left_to_right = n
    n_right_to_left = n
    left_to_right_collisions = 0
    right_to_left_collisions = 0

    while n_left_to_right!= 0 and n_right_to_left!= 0:
        if left_to_right_collisions!= 0:
            right_to_left_collisions += 1
        else:
            n_left_to_right -= 1

        if right_to_left_collisions!= 0:
            left_to_right_collisions += 1
        else:
            n_right_to_left -= 1

    return left_to_right_collisions + right_to_left_collisions

