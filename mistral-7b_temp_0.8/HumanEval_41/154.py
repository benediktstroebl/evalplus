

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
    cars = [[] for _ in range(n)]
    for _ in range(n):
        cars[0].append((0, 1))
    for _ in range(n - 1):
        cars[0].append((2, 0))
    cars[0].append((0, -1))
    for i in range(1, n):
        cars[i] = cars[i-1] + cars[i-1][::-1]
        for j in range(i):
            if cars[j][0] < cars[i][0]:
                cars[i][0] += cars[j][0]
                cars[i][1] += cars[j][1]
    return cars[n-1][0]

