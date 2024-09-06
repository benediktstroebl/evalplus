

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
    # PATTERN:
    # 1. we need two indexes that we can increment to walk along both sides
    # 2. we need two 'speed' variables to keep track of the distance between the two sides
    # 3. the loop is based on the max speed (the faster one), and we check for collisions.

    # PSEUDOCODE:
    # left_idx = 0
    # right_idx = n - 1
    # left_speed = 0
    # right_speed = 0
    # collision_count = 0
    # while left_idx != right_idx:
    #     if left_speed == right_speed:
    #         collision_count += 1
    #         left_speed += 1
    #         right_speed += 1
    #     else:
    #         if left_speed < right_speed:
    #             left_speed += 1
    #         else:
    #             right_speed += 1
    # return collision_count
    pass
