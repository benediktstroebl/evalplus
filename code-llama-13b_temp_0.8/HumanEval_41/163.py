

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
    cars_left_to_right = [1]*n
    cars_right_to_left = [2]*n
    num_collisions = 0
    curr_left_to_right_car_idx = 0
    curr_right_to_left_car_idx = n-1

    while curr_left_to_right_car_idx < curr_right_to_left_car_idx:
        # Look for collisions at the curr_left_to_right_car_idx
        while curr_left_to_right_car_idx < curr_right_to_left_car_idx \
                and cars_left_to_right[curr_left_to_right_car_idx] == 1:
            curr_left_to_right_car_idx += 1

        # Look for collisions at the curr_right_to_left_car_idx
        while curr_left_to_right_car_idx < curr_right_to_left_car_idx \
                and cars_right_to_left[curr_right_to_left_car_idx] == 2:
            curr_right_to_left_car_idx -= 1

        if curr_left_to_right_car_idx < curr_right_to_left_car_idx:
            num_collisions += 1

    return num_collisions

