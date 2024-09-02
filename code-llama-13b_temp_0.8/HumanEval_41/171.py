

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
    cars_left_to_right = [1] * n
    cars_right_to_left = [1] * n

    left_to_right_collisions = 0
    right_to_left_collisions = 0

    while any(cars_left_to_right) and any(cars_right_to_left):
        cars_left_to_right = [c - 1 for c in cars_left_to_right]
        cars_right_to_left = [c - 1 for c in cars_right_to_left]

        while len(cars_left_to_right) > 1 and cars_left_to_right[0] == 0:
            cars_left_to_right = cars_left_to_right[1:]
            right_to_left_collisions += 1

        while len(cars_right_to_left) > 1 and cars_right_to_left[0] == 0:
            cars_right_to_left = cars_right_to_left[1:]
            left_to_right_collisions += 1

    return left_to_right_collisions + right_to_left_collisions

