

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
    # given n = 5, cars 1 and 2 are moving left to right, cars 3 and 4 are moving right to left, 
    # and the distance between the two is l = 7
    # cars 2 and 4 collide at the distance of 0, and car 1 and 3 collide at distance l = 2
    # total collisions = 2
    l = 7
    cars = range(1,n+1)
    collisions = 0
    for c1 in cars: 
        for c2 in cars:
            if c1*c2 == l:
                collisions += 1
    return collisions
