

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
    collisions = 0
    # iterate through cars in odd and even lanes
    for lane in range(0, n*2, 2):
        # find the cars in the lane
        left_car = lane
        right_car = lane + 1
        # start with first pair of cars and continue until all pairs are done
        while right_car < n*2:
            # check if cars collide and update collisions
            if left_car < 0 or left_car > (n-1):
                left_car += 2
                right_car += 2
                continue
            if right_car < 0 or right_car > (n-1):
                left_car += 2
                right_car += 2
                continue
            if left_car == right_car:
                collisions += 1
            left_car -= 2
            right_car += 2
    return collisions
