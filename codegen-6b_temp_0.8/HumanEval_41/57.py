

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
    collisions: int = 0
    if n % 2 == 0:
        return collisions

    for i in range(0, n // 2):
        for j in range(i, n - 1 - i):
            if not i == j:
                pos1: int = (i + 1) + (n - j - 2)
                pos2: int = pos1 + ((n - 1 - j) + i)
                if pos1 % 2 == 0 and pos2 % 2 == 0:
                    collisions += 1
    return collisions

