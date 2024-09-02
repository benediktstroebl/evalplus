

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
    strengths = [random.randint(1, 200) for _ in range(n)]
    speeds = [random.randint(1, 200) for _ in range(n)]
    times = [random.randint(1, 200) for _ in range(n)]

    collisions = 0
    i = 0
    while i < n:
        if is_colliding(strengths[i], speeds[i], times[i]):
            collisions += 1
        i += 1

    return collisions

