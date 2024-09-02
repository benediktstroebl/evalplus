

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
    # Let's try this with n=3
    if n == 3:
        return 1

    # Otherwise, we'll check the next set of n-1 cars in the left-to-right set
    # and the next set of n-1 cars in the right-to-left set
    for i in range(n-1):
        for j in range(i+1, n):
            # If the left-to-right car and the right-to-left car are the same distance
            # from each other, they collide
            if abs(i-j) == n/2:
                return 2

    # If there are no collisions, return 0
    return 0