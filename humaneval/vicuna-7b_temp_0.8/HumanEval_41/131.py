

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
    #n is the number of cars
    #n/2 is the middle of the number of cars

    #creating a list of numbers 0 to n-1
    arr = list(range(n))
    #sorting the list in ascending order
    arr.sort()
    #creating a variable j to check if there is a collision
    j = 0
    #while j is less than or equal to n/2
    while j < (n/2):
        #checking if the first car in the list has passed the middle of the road
        if arr[j] == 0:
            break
        #checking if the last car in the list has passed the middle of the road
        if arr[-j-1] == n-1:
            break
        #if the first and last car haven't passed the middle of the road,
        #there is a collision
        if arr[j] == n-1 or arr[-j-1] == 0:
            j += 1
            #if j is greater than n/2, there is a collision
            if j > n/2:
                return j
        #incrementing j by 1
        j += 1
    return 0