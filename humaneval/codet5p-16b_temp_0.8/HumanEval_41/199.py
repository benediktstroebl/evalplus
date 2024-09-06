

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

    from collections import deque
    cars_left = deque(range(1, n+1))
    cars_right = deque(range(n, 0, -1))
    collisions = 0
    while len(cars_left) and len(cars_right):
        left_car = cars_left.popleft()
        right_car = cars_right.popleft()
        if left_car > right_car:
            collisions += right_car
        elif right_car > left_car:
            collisions += left_car
        else:
            collisions += right_car
            collisions += left_car

    return collisions


