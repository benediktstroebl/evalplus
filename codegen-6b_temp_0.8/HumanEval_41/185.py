

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
    # ~3ms
    collide_count = 0
    for i in range(n):
        x = i * 2
        if i % 2 == 0:
            for j in range(1, n):
                y = j + 1
                if (x + j) % 2 == 1:
                    if x % 2 == 0:
                        collide_count += 1
                    else:
                        y = n - j - 1
                        collide_count += 1
        else:
            for j in range(1, n):
                y = j + 1
                if (x + j) % 2 == 1:
                    if x % 2 == 0:
                        collide_count += 1
                    else:
                        y = n - j - 1
                        collide_count += 1
    return collide_count


