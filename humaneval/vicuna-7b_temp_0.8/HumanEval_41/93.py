

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
    # Assumption: all n are positive integers
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    i, j = 0, 0
    while i < n and j < n:
        if i < n and j == n or i == n and j < n:
            # Left to right car hits right to left car
            collision()
        i += 1
        j += 1
    return n-i-j