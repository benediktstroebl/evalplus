

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

    num_collisions = 0

    # there are two cars moving left to right, and two cars moving right to left
    n_left_to_right = n
    n_right_to_left = n

    while n_left_to_right > 0 and n_right_to_left > 0:

        # if the cars at the leftmost edges collide, then there is one collision
        if n_left_to_right > 0 and n_right_to_left > 0:
            num_collisions += 1
            n_left_to_right -= 1
            n_right_to_left -= 1

        # if the cars at the leftmost edges do not collide, then the leftmost edges
        # of the right to left cars collide with the rightmost edges of the left to right cars
        else:
            num_collisions += n_right_to_left
            n_left_to_right = 0
            n_right_to_left = 0

    return num_collisions

