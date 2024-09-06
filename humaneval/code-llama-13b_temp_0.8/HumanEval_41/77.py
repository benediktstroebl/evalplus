

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
    # n cars driving left to right, n cars driving right to left
    # distance from leftmost car driving right to left to the rightmost car driving left to right
    distance = n * 2
    # one collision for every pair of cars
    # how many cars collided
    collisions = 0
    # cars are moving simultaneously
    for i in range(n):
        # a car driving left to right is positioned
        # distance away from a car driving right to left
        ltr = i
        rtl = distance - i
        # if the cars are positioned such that they collide
        if ltr == rtl:
            # increase collisions by one
            collisions += 1
    # return the number of collisions
    return collisions

