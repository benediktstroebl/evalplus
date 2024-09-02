

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

    assert n >= 2

    collisions = 0
    for i in range(1, n):
        for j in range(n - 1):
            if j == i:
                continue
            left_car = j
            right_car = j + 1
            left_car_distance_before_collision = left_car * 2
            right_car_distance_before_collision = right_car * 2
            left_car_distance_after_collision = left_car * 2 + 1
            right_car_distance_after_collision = right_car * 2 + 1

            left_car_distance_after_collision = max(left_car_distance_after_collision, right_car_distance_after_collision)
            right_car_distance_after_collision = max(left_car_distance_after_collision, right_car_distance_after_collision)

            left_car_distance_after_collision = max(left_car_distance_after_collision, right_car_distance_after_collision)
            right_car_distance_after_
