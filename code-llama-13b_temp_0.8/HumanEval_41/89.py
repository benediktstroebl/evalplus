

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
    l2r = 1
    r2l = 2
    cars = {l2r: {}, r2l: {}}
    for i in range(1, n+1):
        cars[l2r][i] = 2*i-1
        cars[r2l][i] = 2*i
    counter = 0
    left_most_l2r = cars[l2r][1]
    right_most_r2l = cars[r2l][n]
    while left_most_l2r <= right_most_r2l:
        if left_most_l2r in cars[r2l]:
            counter += 1
        left_most_l2r += 1
    return counter

