

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
    for i in range(2 * n):
        for j in range(i + 1, 2 * n):
            if i % 2 == 0:
                if j % 2 == 0:
                    if (i / 2) <= j / 2 <= (i + 1) / 2:
                        collisions += 1
            else:
                if (i + 1) / 2 <= j / 2 <= (i) / 2:
                    collisions += 1
    return collisions

