

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

    # cars are infinitely sturdy and strong; as a result, they continue moving
    # in their trajectory as if they did not collide.
    # Return the number of such collisions.

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    # 5 - 1
    # 6 - 1
    # 7 - 1
    # 8 - 1
    # 9 - 1
    # 10 - 1
    # 11 - 1
    # 12 - 1
    # 13 - 1
    # 14 - 1
    # 15 - 1
    # 16 - 1
    # 17 - 1
    # 18 - 1
    # 19 - 1
    # 20 - 1
    # 21 - 1

    # n = 21

    # def get_collision(n: int):
    #     if n % 2 == 0:
    #         return n / 2 - 1
    #     elif n % 2 != 0:
    #         return n / 2

    # return get_collision(n)

    # print(n % 2)
    # print(n / 2 - 1)
    # print(n / 2)

    # cars are infinitely sturdy and strong; as a result, they continue moving
    # in their trajectory as if they did not collide.
    # Return the number of such collisions.

    if n % 2 == 0:
        return n // 2
    else:
        return n // 2 - 1

