

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

    # The time to collide (in seconds) for left to right driving cars
    left_to_right_time = n * 2
    right_to_left_time = n * 2
    left_to_right_speed = left_to_right_time / (n * 2)
    right_to_left_speed = right_to_left_time / (n * 2)
    collisions = 0

    for i in range(0, n):
        left_to_right_car = left_to_right_speed * i
        right_to_left_car = right_to_left_speed * i
        if left_to_right_car == right_to_left_car:
            collisions += 1
    return collisions
