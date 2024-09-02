

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

    from math import inf
    cars = [[i, inf] for i in range(n)]

    for car in cars:
        car[1] = min(car[1], car[0] + n - car[0])
        car[0] += 1

    return sum(car[0] < car[1] for car in cars)

