

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

    assert n >= 2

    cars = {(i, 0) for i in range(n)}
    while True:
        left_to_right = set()
        right_to_left = set()
        for c in cars:
            if c[1] == 0:
                left_to_right.add(c)
            else:
                right_to_left.add(c)
        if left_to_right and right_to_left:
            left_to_right = {c[0] for c in left_to_right}
            right_to_left = {c[0] for c in right_to_left}
            if left_to_right.intersection(right_to_left):
                return len(left_to_right.intersection(right_to_left))
        for c in left_to_right:
            cars.discard((c[0], 0))
        for c in right_to_left:
            cars.discard((c[0], 1))
        if not cars:
            return 0
        for c in cars:
            
