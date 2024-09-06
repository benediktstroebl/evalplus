

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
    cars = 2*n
    cars_collision = 0
    while cars > 1:
        cars_left = n
        cars_right = n
        cars_left_speed = 1
        cars_right_speed = 1
        while cars_left > 1 or cars_right > 1:
            cars_left -= cars_left_speed
            cars_right -= cars_right_speed
            cars_left_speed -= 1
            cars_right_speed -= 1
            cars_collision += 1
            if cars_left <= 0:
                cars_left = 0
            if cars_right <= 0:
                cars_right = 0
        cars -= 1
    return cars_collision

