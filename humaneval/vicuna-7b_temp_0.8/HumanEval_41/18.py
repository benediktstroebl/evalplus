

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
    # initialize variables
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    left_mover = 0
    right_mover = 0
    total = 0

    # set up conditions to detect collisions
    while (len(left_cars) > 0 and len(right_cars) > 0 and not left_cars[left_mover] == right_cars[right_mover]):
        # determine if left or right car should move
        if left_cars[left_mover] > right_cars[right_mover]:
            # move left car
            left_mover += 1
            total += 1
        else:
            # move right car
            right_mover += 1
            total += 1

    return total