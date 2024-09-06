

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
    # a = n
    # b = n
    # while a > 0:
    #     while b > 0:
    #         if car_race_collision_one_car(a,b):
    #             a -= 1
    #             b -= 1
    #         else:
    #             b -= 1
    #     a -= 1
    #     b = n

    a = [n] * n
    b = [n] * n
    count = 0
    while True:
        if car_race_collision_one_car_refined(a,b):
            count += 1
        else:
            break
    return count
