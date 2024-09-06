

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

    if n % 2 == 0:
        return 0

    n = n - 1
    left_cars = n // 2
    right_cars = n // 2 + 1

    collision = 0
    for lc in range(1, left_cars+1):
        for rc in range(1, right_cars+1):
            if lc + rc > 1:
                collision += 1

    return collision


