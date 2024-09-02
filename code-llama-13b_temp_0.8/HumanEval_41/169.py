

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

    # lets create an array of size 2 * n + 1 and set the middle element to be -n.  this means that the car driving
    # in the left to right direction is at the end of the array and the car driving in the right to left direction
    # is at the beginning of the array

    cars = [0] * (2 * n + 1)
    cars[n] = -n

    # now lets run the cars
    collisions = 0
    for i in range(n - 1, -1, -1):
        # find the next position to the right of the current position
        next_index = i + cars[i]

        # if that position is occupied by a car, there is a collision
        if cars[next_index] < 0:
            collisions += 1
            # we need to determine which car this is
            other_car_index = -cars[next_index]
            # we need to remove both cars from the array
            cars[next_index], cars[other_car_index] = 0, 0

        # if the next position is not occupied, move the car there
        else:
            cars[next_index] = cars[i]
            cars[i] = 0

    return collisions

