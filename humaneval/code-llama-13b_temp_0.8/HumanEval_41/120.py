

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
    car_distances = list(range(1, n+1))
    left_to_right_cars = car_distances
    right_to_left_cars = [-i for i in car_distances]
    left_to_right_collisions = 0
    right_to_left_collisions = 0

    while len(left_to_right_cars) > 1:
        left_to_right_collisions += collide(left_to_right_cars)
    while len(right_to_left_cars) > 1:
        right_to_left_collisions += collide(right_to_left_cars)
    return left_to_right_collisions + right_to_left_collisions

