

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
        for j in range(i+1, n):
            if abs(i-j) == n//2:
                continue
            if (i-j) % 2 != 0:
                continue
            if cars_on_left[i] and cars_on_right[j]:
                return n
    return 0