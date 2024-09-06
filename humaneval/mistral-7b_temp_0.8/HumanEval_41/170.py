

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
    collision_count = 0
    l = []
    r = []
    for i in range(n):
        l.append(i)
    for i in range(n):
        r.append(n-i)
    while l:
        l.append(l.pop(0)-1)
        r.append(r.pop(0)-1)
        if l[0] == r[0]:
            collision_count += 1
        elif l[0] < r[0]:
            l.pop(0)
        else:
            r.pop(0)
    return collision_count

