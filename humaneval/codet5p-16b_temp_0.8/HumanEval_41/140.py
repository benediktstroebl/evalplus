

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

    n_cars = n

    left_to_right_cars = [0] * (n_cars + 1)
    right_to_left_cars = [0] * (n_cars + 1)

    left_to_right_cars[1] = n_cars
    right_to_left_cars[-2] = n_cars

    cars_collided = 0

    for i in range(2, n_cars + 1):
        left_to_right_cars[i] = left_to_right_cars[i - 1] - 1
        right_to_left_cars[-i] = right_to_left_cars[-i + 1] + 1

        if left_to_right_cars[i] < 0:
            right_to_left_cars[i] += 1
            left_to_right_cars[i] = 0

        if right_to_left_cars[i] >= n_cars:
            right_to_left_cars[i] = n_cars - 1
            left_to_right_cars[i] = n_cars
