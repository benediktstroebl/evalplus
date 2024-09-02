

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
    if n < 1:
        return 0

    # initially all cars start at the same time, so they are at distance 0 from
    # each other
    distance = 0

    # list of distances from start to finish for both sets of cars.  Each set
    # contains n entries.
    forward_distances = [distance] * n
    backward_distances = [distance] * n

    # simulate the cars driving, and count the number of collisions.  As we
    # do so, we update the distance from start to finish
    collisions = 0
    for _ in range(n - 1):
        # we're moving forwards (left to right)
        distance += 1
        forward_distances = [d + 1 for d in forward_distances]

        # we're moving backwards (right to left)
        backward_distances = [d - 1 for d in backward_distances]

        # count the collisions
        collisions += count_collisions(forward_distances, backward_distances)

    return collisions

