

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
    # N is the sum of the number of cars moving left to right and the number of cars moving right to left
    N = n**2
    for i in range(n//2):
        if n % 2 == 0:
            # left cars
            j = i + n//2
            while j < N//2 and (j-i)%i != 0:
                j += n//2
            while j >= i and (j-i)%i == 0:
                j -= n//2
        else:
            # right cars
            j = i + n//2
            while j < N//2 and (j-i)%i != 0:
                j += n//2
            while j >= i and (j-i)%i == 0:
                j -= n//2
    return 0