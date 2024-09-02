

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
    # If n is odd, then the collision will happen between the two middle cars.
    if n % 2 == 1:
        # The two middle cars will hit each other.
        return 2
    else:
        # If n is even, the collision will happen between the two middle cars and
        # the two outer cars.
        return 3
