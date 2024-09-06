

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
    assert type(n) == int
    cars_left_to_right = 2 * n
    cars_right_to_left = 2 * n
    cars_left_to_right_speed = 2 * n
    cars_right_to_left_speed = 2 * n
    collisions = 0
    # Your code goes here
    # You are welcome to use any data structures
    for i in range(2 * n):
        if cars_right_to_left_speed > cars_left_to_right_speed:
            cars_left_to_right_speed += 1
            cars_right_to_left_speed -= 1
        else:
            cars_right_to_left_speed += 1
            cars_left_to_right_speed -= 1
        if cars_right_to_left_speed == cars_left_to_right_speed:
            collisions += 1
    return collisions

