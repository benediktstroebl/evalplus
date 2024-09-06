

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
    # Write your code here
    l = n
    r = 1
    res = 0
    while l > 0 and r > 0:
        if l % 2 != 0:
            l = l // 2 + l // 2 + 1
        else:
            l = l // 2
        if r % 2 != 0:
            r = r // 2 + r // 2 + 1
        else:
            r = r // 2
        res += l * r
    return res

