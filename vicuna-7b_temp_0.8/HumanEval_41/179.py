

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
    car_speed = 1
    min_dist = 10
    min_dist_idx = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(i-j) > min_dist:
                dist = abs(i-j)
                if dist < min_dist_idx:
                    min_dist_idx = dist
                if dist <= car_speed:
                    break
            elif min_dist_idx <= car_speed:
                min_dist_idx += car_speed
    return min_dist_idx