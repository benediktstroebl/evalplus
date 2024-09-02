

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
    # if n < 1, return 0
    if n < 1:
        return 0

    # find the midpoint of the line
    midpoint = (0, 0)

    # the first set of cars is (1, 1), the second set of cars is (-1, -1)
    first_cars = (1, 1)
    second_cars = (-1, -1)

    # let's compute the position of the midpoint after 1 step
    midpoint_1 = midpoint + (0, 1)

    # keep updating the midpoint and the cars
    while True:
        # find the position of the cars after 1 step
        first_cars_1 = first_cars + (0, 1)
        second_cars_1 = second_cars - (0, 1)

        # check if there's a collision
        if first_cars_1[0] == second_cars_1[0] or first_cars_1[1] == second_cars_1[1]:
            return 1

        # update the midpoint and the cars
        midpoint_1 = midpoint_1 + (0, 1)
        first_cars = first_cars_1
        second_cars = second_cars_1

    # there were no collisions
    return 0