

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
    # List of cars moving left to right
    left = range(n)
    # List of cars moving right to left
    right = range(n - 1, -1, -1)
    # Collision count
    collisions = 0
    # Loop while cars can still move
    while left and right:
        # Move the cars that can
        left.pop()
        right.pop()
        # Increment collision count
        collisions += 1
    # Return collisions
    return collisions
