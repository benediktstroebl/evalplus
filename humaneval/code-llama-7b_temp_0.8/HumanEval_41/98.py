

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

    # 2d array
    n = n * 2
    # a, b, c = 1, 0, 1
    # r = [0, a, b, c]
    # for _ in range(n - 4):
    #     r.append(r[-1] + r[-4])

    r = [0] * n
    for i in range(1, n):
        r[i] = r[i - 1] + r[0]

    # sum_cars = [0] * n
    # for i in range(1, n):
    #     sum_cars[i] = sum_cars[i - 1] + r[i]

    # return sum(i for i in range(n) if sum_cars[i] < sum_cars[n - 1 - i])

    return r[n // 2]


