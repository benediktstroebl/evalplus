

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

    from itertools import permutations
    from collections import Counter

    m = []
    for _ in range(n):
        m.append([i for i in range(n)])

    lst = []
    for i in range(n):
        lst += [i]

    l = list(permutations(lst))

    c = Counter()

    for i in l:
        for j in range(n-1):
            if m[i[j]][i[j+1]] == i[j+1]:
                continue
            else:
                c[j] += 1

    return sum(c.values())

