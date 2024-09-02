

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
    # Your code goes here
    if n < 1:
        return 0
    if n == 1:
        return 1
    left_cars = (range(n))
    right_cars = (range(n))[::-1]
    left_car_count = sum(1 for car in left_cars if car != n)
    right_car_count = sum(1 for car in right_cars if car != n)
    if left_car_count != right_car_count:
        return 1
    for i in range(1, n):
        if left_cars[i] == n:
            left_car_count -= 1
        elif right_cars[i] == n:
            right_car_count -= 1
        if left_car_count != right_car_count:
            return 1
    return 0