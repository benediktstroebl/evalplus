

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
    if n < 1:
        raise ValueError("n must be greater than 0, but found %s" % n)

    collisions = 0
    for i in range(n):
        for j in range(n - 1):
            if cars[i].lane == "right" and cars[j].lane == "left":
                if cars[i].x < cars[j].x:
                    collisions += 1
    return collisions
