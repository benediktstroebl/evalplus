

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
    # n will be even
    n = n // 2

    # calculate the minimum distance between two cars
    min_distance = 1
    for i in range(n - 1):
        min_distance = min(min_distance, abs(i - (n // 2)))

    # calculate the maximum distance between two cars
    max_distance = 1
    for i in range(n - 1):
        max_distance = max(max_distance, abs(n - i - 1))

    # calculate the number of collisions
    collision_count = (n ** 2) - (min_distance ** 2) - (max_distance ** 2)
    return collision_count

