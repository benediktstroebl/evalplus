

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
    # n must be odd since the two sets of cars are moving in opposite directions
    # and the first car on the left is moving at a distance of (n-1)/2 from the starting point.
    if n % 2 == 1:
        left_start = (n - 1) / 2
    else:
        left_start = n / 2

    # This loop counts the number of collisions
    collisions = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i > 1 and j > 1:
                # The two cars on the left
                if i - 1 > left_start and j - 1 > left_start:
                    collisions += 1
            elif i > j:
                # The two cars on the right
                if i - j + 1 > left_start:
                    collisions += 1

    return collisions
