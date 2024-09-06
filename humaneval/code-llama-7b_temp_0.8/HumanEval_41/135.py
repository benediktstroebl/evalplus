

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
    ans = 0
    cars = [1] * n
    t = 0
    while cars != [0] * n:
        t += 1
        for i in range(n):
            cars[i] -= 1
            if i > 0 and cars[i-1] == 0:
                ans += 1
            if i < n - 1 and cars[i+1] == 0:
                ans += 1
            if cars[i] == 0:
                cars[i] = 1

    return ans

