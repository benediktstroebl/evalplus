

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
    a = [0, 0]
    for i in range(n):
        a = a + [a[-1] + 1]
    b = [0, 0]
    for i in range(n):
        b = b + [b[-1] + 1]
    # print(a)
    # print(b)
    c = [0, 0]
    for i in range(n):
        c = c + [min(a[i], b[i])]
    # print(c)
    sum = 0
    for i in range(n):
        sum = sum + c[i]
    return sum


