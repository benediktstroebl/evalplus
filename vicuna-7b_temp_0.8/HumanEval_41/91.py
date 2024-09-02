

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
    # let's write the two sets of n cars and check for collisions
    cars_moving_left_to_right = [f'{i*1000000000000}L' for i in range(n)]
    cars_moving_right_to_left = [f'{i*1000000000000}R' for i in range(n)]
    collision_count = 0
    for i in range(n):
        for j in range(i, n):
            if cars_moving_left_to_right[i] == cars_moving_left_to_right[j]:
                if cars_moving_right_to_left[j] == cars_moving_right_to_left[i]:
                    collision_count += 1
    return collision_count