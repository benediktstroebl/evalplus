

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

    import math
    n_left, n_right = 0, 0
    for _ in range(n):
        n_left += 1
        n_right += 1
        left_y, right_y = car_race_collision.collision_time_calculator(n_left, n_right)
        n_left += 1
        n_right -= 1
        left_y, right_y = min(left_y, car_race_collision.collision_time_calculator(n_left, n_right)[0]), \
                          max(right_y, car_race_collision.collision_time_calculator(n_left, n_right)[1])
        n_left -= 1
        n_right += 1
        left_y, right_y = min(left_y, car_race_collision.collision_time_calculator(n_left, n_right)[0]), \
                          max(right_y, car_race_collision.collision_time_calculator(n_left, n_right)[1
