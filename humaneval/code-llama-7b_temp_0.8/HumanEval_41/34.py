

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
    l = 0
    r = n-1
    ret = 0
    while l<n and r>=0:
        if l==r:
            return ret
        if l<r:
            if l==r-1:
                ret+=1
                l+=1
                r-=1
                continue
            if l<r-1:
                if l==r-2:
                    ret+=1
                    l+=1
                    r-=1
                    continue
            l+=1
            r-=1
        if l>r:
            if l==r+1:
                ret+=1
                l+=1
                r-=1
                continue
            if l>r+1:
                if l==r+2:
                    ret+=1
                    l+=1
                    r-=1
                    continue
            l-=1
            r+=1
    return ret

