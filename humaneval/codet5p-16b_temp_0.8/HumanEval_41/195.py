

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

    assert n >= 2, 'At least two cars are needed'

    n = min(n, int(1e9))
    cars = [i for i in range(1, n + 1)]

    left_to_right = cars
    right_to_left = []

    def move(i: int, l2r: list, r2l: list):
        if i < n:
            l2r.append(i + 1)
            move(i + 1, l2r, r2l)
            r2l.append(i + 1)
            move(i + 1, l2r, r2l)

    move(0, left_to_right, right_to_left)

    return len([i for i in range(1, n + 1) if left_to_right.index(i) == right_to_left.index(i)])
