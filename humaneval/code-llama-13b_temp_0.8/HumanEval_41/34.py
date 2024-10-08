

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
    total_cars = 2 * n
    num_collisions = 0
    for car in range(total_cars):
        direction_left_to_right = car < n
        if direction_left_to_right:
            # we are left to right
            # which means, next car position would be 2n -1 away
            next_position = (2*n) - car - 1
        else:
            # right to left
            # next position would be car+1
            next_position = car + 1
        if car == next_position:
            continue
        else:
            num_collisions += 1

    return num_collisions

