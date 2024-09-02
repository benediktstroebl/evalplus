

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
    if n <= 1:
        return 0
    else:
        # precompute values that will be used later
        min_x1 = max(n//2 - 10, 0)
        min_x2 = n - 20
        for i in range(n-1):
            for j in range(i+1, n):
                # we don't need to check the (i,i+1) or (j,j-1) cases
                # since they are symmetric
                if j > i+2:
                    # compute the distance between cars
                    d = abs(min_x2 - (i+1) * 10) - abs(min_x1 - j * 10)
                    # if the distance is greater than 2, there is a collision
                    if d > 2:
                        return d
        return 0
