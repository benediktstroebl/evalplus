

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
    if n < 2:
        return 0
    if n == 2:
        return 1
    left_cars = [i for i in range(n)]
    right_cars = [n-i-1 for i in range(n)]
    collision_count = 0
    for i in range(1, n):
        for j in range(1, n-i-1):
            if i not in left_cars and j not in left_cars and i not in right_cars and j not in right_cars:
                collision_count += 1
    return collision_count