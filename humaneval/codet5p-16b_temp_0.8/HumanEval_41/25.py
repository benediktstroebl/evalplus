

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

    left_cars = [0 for _ in range(n)]
    right_cars = [0 for _ in range(n)]
    while True:
        for i, left in enumerate(left_cars):
            if left == 0:
                left_cars[i] = left_cars[i-1] + 1
        for i, right in enumerate(right_cars):
            if right == 0:
                right_cars[i] = right_cars[i-1] + 1
        if left_cars == right_cars:
            return left_cars.count(n)
