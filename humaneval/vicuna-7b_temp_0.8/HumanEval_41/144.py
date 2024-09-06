

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
    # example:  car_race_collision(4)
    # returns 1
    #
    # 4 8 15 16
    # 5 10 15 16
    # 6 11 16 17
    # 7 12 17 18
    #
    #
    # 4 16 17 18
    # 5 8 9 10
    # 6 4 5 6
    # 7 11 12 13
    #

    #
    # 4 16 17 18
    # 5 8 9 10
    # 6 11 12 13
    # 7 4 5 6
    #
    #
    # 4 8 15 16
    # 5 10 15 16
    # 6 11 16 17
    # 7 12 17 18

    #
    # 4 16 17 18
    # 5 8 9 10
    # 6 11 12 13
    # 7 4 5 6
    #
    #
    # 4 8 15 16
    # 5 10 15 16
    # 6 11 16 17
    # 7 12 17 18

    n_cars_left = sum(1 for _ in range(n))
    n_cars_right = sum(1 for _ in range(n))
    if n_cars_left > n_cars_right:
        return 0

    i = n // 2
    j = n // 2

    while i < n - 1 and j < n - 1:
        if (j - i) % 2 == 0:
            continue
        else:
            if (j - i) // 2 + 1 <= n_cars_left and (j
