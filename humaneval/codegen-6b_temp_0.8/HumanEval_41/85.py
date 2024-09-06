

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
    assert(n >= 2), 'Must have at least two cars'
    candidates = np.zeros(n)
    c = 0
    while True:
        combinations = combinations(-c, n)
        for x in combinations:
            temp = np.copy(x)
            if np.all(temp > n/2):
                candidates += temp
                break

        c += 1
        if c > n:
            break
    return np.sum(candidates)
