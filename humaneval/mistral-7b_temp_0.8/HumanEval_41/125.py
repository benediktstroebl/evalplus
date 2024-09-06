

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
    i = 0
    while 1:
        i = i + 1

        # left-to-right cars
        x = 0
        for _ in range(n):
            x = x + 1

        # right-to-left cars
        y = 0
        for _ in range(n):
            y = y + 1

        if x == y:
            print(i)
            break
