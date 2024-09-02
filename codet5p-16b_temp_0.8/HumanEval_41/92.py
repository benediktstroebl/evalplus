

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

    collisions = 0

    for i in range(n):
        left_car_x = i
        right_car_x = n - 1 - i
        left_car_y = 0
        right_car_y = 0

        while left_car_y >= right_car_y and left_car_y >= 0:
            left_car_y += 1
            right_car_y += 1
            if left_car_y == right_car_y:
                collisions += 1

    return collisions

