

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
    car_position_map = {}
    for i in range(n):
        car_position_map[i] = 0

    for i in range(n):
        car_position_map[i] += 1
        car_position_map[n-i-1] += 1
    count = 0
    for i in range(n):
        for j in range(i, n):
            if car_position_map[i] < car_position_map[j]:
                count += 1
    return count
