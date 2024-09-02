

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

    """
    2 cars collide if they are one car apart.
    We can solve this problem by simulating the cars movement and outputting the number of collisions

    """

    n_l = [0] * n
    n_r = [0] * n

    c = 0

    for i in range(n):
        n_r[i] = 2 * i
        n_l[i] = n - 2 * i - 1

    for i in range(n):
        for j in range(i, n):
            if n_r[i] == n_l[j]:
                c += 1

    return c

