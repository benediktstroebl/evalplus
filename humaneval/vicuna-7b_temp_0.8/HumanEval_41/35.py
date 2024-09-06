

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
    if n < 2:
        return 0
    
    mid = n // 2
    
    # check for collisions on the left side
    for i in range(mid, n-1):
        for j in range(i-1, mid-1):
            # check for head-on collision
            if (i, j) == (mid, mid) or (i, j) == (mid+1, 0) or (i, j) == (0, mid):
                return 1
            # check for side-by-side collision
            elif (i, j) == (mid-1, 0) or (i-1, j) == (mid, 0) or (i-1, j) == (mid, 1) or (i, j-1) == (mid-1, 1):
                return 1
    
    # check for collisions on the right side
    for i in range(mid+1, n):
        for j in range(i, mid):
            # check for head-on collision
            if (i, j) == (mid, mid) or (i, j) == (mid+1, 0) or (i, j) == (0, mid):
                return 1
            # check for side-by-side collision
            elif (i-1, j) == (mid, 1) or (i-1, j) == (mid, 0) or (i-1, j-1) == (mid+1, 0) or (i-1, j-1) == (mid+1, 1):
                return 1
    
    return 0
