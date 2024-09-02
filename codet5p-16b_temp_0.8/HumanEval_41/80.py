

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

    assert n > 1
    def _collision_helper(cars: list):
        return sum(1 for i in range(len(cars)-1) for j in range(i+1, len(cars)) if cars[i][1] < cars[j][1] and cars[i][0] < cars[j][0])
    return _collision_helper(sorted([(i%2, i) for i in range(n)], key=lambda t: t[1]))
