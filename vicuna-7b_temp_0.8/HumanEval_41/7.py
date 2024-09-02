

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
    for i in range(n):
        for j in range(n):
            if i == n-j-1:
                # this is a collision if the leftmost car of the first set hits the rightmost car of the second set
                return 1
            elif i == j+1:
                # this is a collision if the leftmost car of the first set hits the leftmost car of the second set
                return 1
            else:
                # this is a collision if the second set hits the first set
                return 1
    return 0