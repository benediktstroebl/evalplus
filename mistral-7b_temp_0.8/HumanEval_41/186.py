

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

    # number of cars
    n = int(input())
    # distance between cars
    d = float(input())
    # distance between the two sides of the road
    r = float(input())
    # cars moving from left to right
    a = [float(x) for x in input().split()]
    # cars moving from right to left
    b = [float(x) for x in input().split()]
    # number of cars that collided
    collisions = 0
    # start of the loop to get the distance between each car
    i = 0
    # end of the loop
    while i < n:
        # calculate the distance between the cars
        distance_left = a[i] + d
        distance_right = b[i] + d
        # loop to check if there is a collision
        j = 0
        while j < n:
            # if there is a collision
            if distance_left <= r and distance_right <= r:
                # increment the number of collisions
                collisions += 1
            # check the distance between the cars
           
