

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

    if n == 0:
        return 0

    n = 2 * n  # this is so we always have at least 2 cars
    cars_left = n
    cars_right = n
    left_to_right = True
    right_to_left = False
    result = 0

    while cars_left > 1:
        if left_to_right:
            cars_left -= 1
            result += 1
        if right_to_left:
            cars_right -= 1
            result += 1

        if cars_left > 1:
            left_to_right = not left_to_right
            right_to_left = not right_to_left
        elif cars_left == 1:
            if left_to_right:
                left_to_right = False
            elif right_to_left:
                right_to_left = False
            break

        if cars_right > 1:
            left_to_right = not left_to_right
            right_to_left = not right_to_left
        elif cars_right == 1:
            if left_
