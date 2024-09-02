

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
    number_of_collisions = 0
    small_car = 0
    large_car = n-1
    small_car_speed = 1
    large_car_speed = 1
    while small_car < n and large_car >= 0:
        if small_car_speed > large_car_speed:
            large_car_speed += 1
            small_car_speed = 1
        elif small_car_speed < large_car_speed:
            small_car_speed += 1
            large_car_speed = 1
        if small_car_speed == large_car_speed:
            number_of_collisions += 1
            small_car_speed = 1
            large_car_speed = 1
        small_car += 1
        large_car -= 1
    return number_of_collisions
