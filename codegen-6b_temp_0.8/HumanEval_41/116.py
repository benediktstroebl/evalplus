

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
    i = 0
    while i < n:
        collide = False
        for j in range(i, n):
            if j > i:
                if i * j == 1:
                    collide = True
                    break
            for k in range((j + 1) % n):
                if abs(i - j) == abs(i - k) and i * k == j * i:
                    collide = True
                    break
        if not collide:
            break
        i += 1
    return i
