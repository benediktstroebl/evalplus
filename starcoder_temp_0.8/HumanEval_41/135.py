

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
    if n % 2!= 0:
        raise ValueError("n must be divisible by 2")
    left_cars = [True] * n
    right_cars = [True] * n
    n_collisions = 0
    while all(left_cars) and all(right_cars):
        for i in range(len(left_cars)):
            if left_cars[i] and right_cars[i]:
                left_cars[i] = False
                right_cars[i] = False
                n_collisions += 1
    return n_collisions
