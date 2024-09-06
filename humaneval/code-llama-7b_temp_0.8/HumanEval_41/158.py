

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

    # a car is defined as a tuple of (position, velocity)
    # velocity is a boolean indicating whether it's moving left to right
    cars = [(i, True) for i in range(n)] + [(i, False) for i in range(n)]

    collisions = 0
    for step in range(n * 2 * n + 1):
        cars = [(pos + vel * step, vel) for (pos, vel) in cars]
        for i in range(len(cars) - 1):
            for j in range(i + 1, len(cars)):
                if cars[i][0] == cars[j][0] and cars[i][1] != cars[j][1]:
                    collisions += 1
    return collisions
