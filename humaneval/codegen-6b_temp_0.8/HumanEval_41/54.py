

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
    # the distance between the cars, initialized to -1
    ca = [-1]*n
    # the distance between the cars, initialized to -1
    cb = [-1]*n
    # the distance between the cars, initialized to -1
    cc = [-1]*n
    # the distance between the cars, initialized to -1
    cd = [-1]*n

    # the first five cars will be moving to the left, the other five to the right
    # and they will start out as the right side of the line
    for i in range(0,5):
        ca[i] = n-i-1
        cb[i] = i
        cc[i] = n-i-2
        cd[i] = i+1

    # the distance between the cars is determined by their positions
    for i in range(5,n-5):
        ca[i] = i-5
        cb[i] = i+5
        cc[i] = i-4
        cd[i] = i+4

    # the collision has to be between two cars that are moving the same direction
    for i in range(0,n-10,2):
        if ca[i]==ca[i+1] and cb[i]==cb[i+1] and cc[i]==cc[i+1]:
            return(ca[i],cb[i])
        if cc[i]==cc[i+1] and cd[i]==cd[i+1] and ca[i]==ca[i+1]:
            return(ca[i],cd[i])
        if cd[i]==cd[i+1] and ca[i]==ca[i+1] and cb[i]==cb[i+1]:
            return(cb[i],cd[i])

