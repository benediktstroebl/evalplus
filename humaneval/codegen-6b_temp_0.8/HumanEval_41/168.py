

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
    from collections import defaultdict
    speed_count_dict = defaultdict(int)

    for i in range(n):
        speed_count_dict[(i, i)] += 1
        speed_count_dict[(-i, -i)] += 1

    return sum(1 for k, v in speed_count_dict.items() if v > 1)
