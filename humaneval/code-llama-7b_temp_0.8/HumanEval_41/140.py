

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

    # There are n cars on each side
    num_cars_left = n
    num_cars_right = n

    # To start, there is only one collision
    num_collisions = 1

    # When cars are infinitely far apart, there is no more collisions
    while num_cars_left > 0 and num_cars_right > 0:

        # A collision occurs if cars from opposite sides are in the same position
        # At the beginning, the cars are infinitely far apart and hence no collision.
        if num_cars_left == num_cars_right:
            num_collisions += 1

        # Both sides move at the same speed; hence we can just check one side
        num_cars_left -= 1
        num_cars_right += 1

    return num_collisions
