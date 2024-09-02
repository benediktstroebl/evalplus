

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
    total_collision = 0
    #check if it's possible for the cars to collide
    for i in range(n):
        for j in range(n, n-i+1):
            #find the middle position of the cars
            middle_pos = (i+j)//2
            #check if the two cars are passing through the middle position
            if (i%2==0 and j%2==0) or (i%2==1 and j%2==1) or (i%2==0 and j%2==1) or (i%2==1 and j%2==0):
                #check if the two cars are passing through the middle position in the same direction
                if abs(i-j)<1:
                    total_collision +=1
    return total_collision
