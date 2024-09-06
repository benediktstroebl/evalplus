

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
    total_collisions = 0
    failed_midpoint = False

    for i in range(n):
        for j in range(n):

            # if we've already found a collision we don't need to check
            # the collisions with this car
            if failed_midpoint:
                break

            # if we've already found a collision we don't need to check
            # the collisions with this car
            if i == j:
                continue

            # if we've already found a collision we don't need to check
            # the collisions with this car
            if abs(i - j) < 2:
                continue

            # if we've already found a collision we don't need to check
            # the collisions with this car
            if abs(i - j) > n / 2:
                continue

            # if we've already found a collision we don't need to check
            # the collisions with this car
            if i < j:
                continue

            if j > i + 1:
                # we are in the same lane, so if we're between the two cars, we
                # check the midpoint between the two
                midpoint = (i + j) // 2
            else:
                # we are not in the same lane, so we check if the midpoint is in
                # the correct lane
                if i > n:
                    # if our index is over n, we are in the right lane
                    midpoint = i + n
                    if midpoint < j:
                        # if the midpoint is between our car and the car in question
                        # then we don't need to check the other lane
                        continue
                else:
                    # if our index is less than n, we are in the left lane
                    midpoint = j + n
                    if midpoint < i:
                        # if the midpoint is between our car and the car in question
                        # then we don't need to check the other lane
                        continue
                
            # if the midpoint is colliding with this car, we increment the collision count
            if abs(i - midpoint) < 3 and abs(j - midpoint) < 3:
                total_collisions += 1
                failed_midpoint = True
                
    return total_collisions

