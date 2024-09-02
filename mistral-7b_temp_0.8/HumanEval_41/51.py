

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

    # Get two cars' positions after colliding
    def collide(c1, c2):
        if c1 > c2:
            return (c2, c1)
        else:
            return (c1, c2)

    # Get the number of cars moving left and right
    l, r = 0, 0
    for i in range(n):
        if i % 2 == 0:
            l += 1
        else:
            r += 1

    # Keep track of which car is moving left and right
    left, right = [0] * (l + r), [0] * (l + r)

    # Track where the car is on the road
    i = 0
    while i < l + r:
        if i % 2 == 0:
            left[i // 2] = i
            i += 1
        else:
            right[i // 2] = i
            i += 1

    # Track which car is moving left and right
    while right[0] < left[-1]:
       
