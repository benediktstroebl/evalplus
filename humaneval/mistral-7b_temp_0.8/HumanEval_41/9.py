

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
    def moving_right_to_left(dist, speed, pos):
        if pos == dist:
            return 0
        return (dist - pos) // speed

    return sum(
        moving_right_to_left(dist, speed, pos)
        for i in range(n)
        for j in range(n)
        if i != j
        for dist, speed, pos in (
            (j + 1, i, 0),
            (j + 1, i, 0),
            (i + 1, j, 0),
        )
    )

