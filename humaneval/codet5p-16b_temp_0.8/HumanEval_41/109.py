

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

    assert 0 <= n <= 1000, 'n should be between 0 and 1000'

    counter = 0
    for i in range(n):
        for j in range(n):
            if i!= j:
                if (i + 1) % 2 == (j - 1) % 2:
                    counter += 1
    return counter

