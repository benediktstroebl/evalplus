

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
    assert n >= 0 and isinstance(n, int)
    assert n % 2 == 0

    # Figure out which side is moving the fastest.  The other side will move
    # the same speed.
    # Finding the maximum element in a list is O(n log n), so we want to find the
    # maximum from one side first.
    max_i = 0
    max_v = 0
    for i in range(n):
        if abs(i - n//2) < max_v:
            continue
        if max_v < abs(i - n//2):
            max_i = i
            max_v = abs(i - n//2)
    if n % 4 == 0:
        # One side is moving 1 unit faster.  Find the second largest element.
        max_v = 0
        for i in range(n):
            if abs(i - n//2) < max_v:
                continue
            if max_v < abs(i - n//2):
                max_i = i
                max_v = abs(i - n//2)
        return (n//2 - max_i) // 2
    if n % 4 == 1:
        # One side is moving 1 unit slower.  Find the second smallest element.
        min_i = 0
        min_v = 2**31
        for i in range(n):
            if abs(i - n//2) > min_v:
                continue
            if min_v > abs(i - n//2):
                min_i = i
                min_v = abs(i - n//2)
        return (n//2 - min_i) // 2
    if n % 4 == 2:
        # Both sides are moving the same speed.
        return n // 2
