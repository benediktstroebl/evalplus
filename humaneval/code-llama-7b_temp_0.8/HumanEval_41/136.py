

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
    distance_between_cars = 100
    start_position = 1
    number_of_collisions = 0
    for i in range(n):
        cars_on_left = start_position
        cars_on_right = start_position + distance_between_cars
        start_position += distance_between_cars

        while abs(cars_on_left - cars_on_right) >= distance_between_cars:
            cars_on_left += 1
            cars_on_right -= 1

        number_of_collisions += 1

    return number_of_collisions

