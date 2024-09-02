

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
    def helper(n, left_to_right, right_to_left):
        # if we only have 1 car or zero cars, there cannot be any collisions
        if n <= 1:
            return 0
        # otherwise, it's exactly the number of collisions for all the cars except the last one
        # plus the number of collisions involving the last car
        return helper(n - 1, left_to_right, right_to_left) + num_collisions_single_car(left_to_right, right_to_left)

    return helper(n, n, 1)

