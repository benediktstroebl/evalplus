

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
    if n == 2:
        return 1

    d = n // 2
    left_speed = d
    right_speed = n - d - 1

    left = [0] * d
    right = [0] * (n - d - 1)

    for i in range(d):
        left[i] = 1

    for j in range(d, n - 1):
        right[j - d] = 1

    for i in range(d):
        for j in range(d, n - 1):
            if i != j and left[i - 1] == 1 and right[j - d] == 1:
                if abs(left[i - 1] - right[j - d]) <= d:
                    return 1

    for i in range(d):
        for j in range(d, n - 1):
            if i != j and left[i - 1] == 1 and right[j - d] == 0:
                return 1

    return 0