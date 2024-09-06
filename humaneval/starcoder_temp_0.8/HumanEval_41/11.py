

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

    # there is no collision if there are no cars
    if n == 0:
        return 0

    # take the car that starts at 0, and move it one step, then move the other car
    # that starts at n - 1 and move it one step.   We use the modulus operator
    # here, so that we can count collisions if the cars started on either side of 0
    collisions = 0
    for car1, car2 in zip(range(n), range(n - 1, -1, -1)):
        if car1 == car2:
            collisions += 1
    return collisions
