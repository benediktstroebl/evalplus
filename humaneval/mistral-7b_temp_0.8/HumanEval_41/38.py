

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
    # TODO: add a function that takes an int n as input,
    # and returns the number of collisions that would occur if there were n cars
    # moving left to right and n cars moving right to left
    # on a perfectly straight, infinitely long road.
    #
    # HINT: Note that a car moving at speed s will travel distance s
    # in one time unit.  Then, use that to determine the time until the two cars
    # collide.  You may find the "range" function useful here.

    left_speed = 0
    right_speed = 0
    number_of_collisions = 0

    if left_speed > right_speed:
        number_of_collisions = 0

    elif left_speed < right_speed:
        number_of_collisions = 0

    elif left_speed == right_speed:
        number_of_collisions = 1

    return number_of_collisions

