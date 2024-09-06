

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

    from collections import deque
    l1 = deque()
    l2 = deque()
    for _ in range(n):
        l1.append(1)
        l2.append(-1)

    count = 0
    while l1:
        num_l1 = l1.popleft()
        num_l2 = l2.popleft()
        if num_l1 > 0 and num_l2 < 0:
            count += 1
        else:
            l1.append(num_l1)
            l2.append(num_l2)
    return count
