

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
    #initialize list of collions
    collisions = []

    #loop through each car moving right to left
    for i in range(n,0,-1):
        #loop through each car moving left to right
        for j in range(n):
            #if the car is colliding, add collision to the list of collisions
            if (i - j) % (abs(i - j)) == 0:
                collisions.append(i)

    #return the number of collisions
    return len(collisions)

