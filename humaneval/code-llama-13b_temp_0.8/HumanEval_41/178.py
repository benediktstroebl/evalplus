

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

    # For all cars that are driving left to right,
    # i.e., all cars in range(n),
    # their x-axis coordinate is their index.
    # Their y-axis coordinate is 0.
    #
    # For all cars that are driving right to left,
    # i.e., all cars in range(n, 2n),
    # their x-axis coordinate is 2n - their index.
    # Their y-axis coordinate is 2n.

    # So, the car at index i collides with the car at index j
    # if and only if they have the same x-axis coordinate,
    # i.e., if and only if
    #
    # i % n == j % n

    # Let's call the car at index i the car at coordinate (i,0).
    # Let's call the car at index j the car at coordinate (j,2n).
    #
    # We want to count the number of collisions, which is the
    # number of coordinates (x,y) where there is a car at coordinate
    # (x,0) and a car at coordinate (x,2n).  These are exactly the
    # coordinates where y = 0.  So, we can do a one-pass algorithm
    # as follows:

    collision_count = 0
    y = 0
    for x in range(1, 3*n):
        # for each x, we first need to count the number of cars at (x,y)
        # (where y = 0).
        car_count = 0
        for i in range(x % n, 3*n, n):
            car_count += 1

        # Then, we need to count the number of cars at (x,2n)
        for j in range(x % n, 3*n, n):
            car_count -= 1

        # Then, the number of collisions is the number of cars at (x,y)
        # where y = 0, i.e., the number of cars at (x,0).
        collision_count += car_count

    return collision_count

