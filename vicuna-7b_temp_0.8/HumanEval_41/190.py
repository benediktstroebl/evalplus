

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
    if n < 2:
        return 0
    if n == 2:
        return 1

    # Make a list of car indices, left to right
    car_indices = range(n)
    car_indices.reverse()

    # Calculate the number of collisions using dynamic programming
    collisions = 0
    for i in range(n):
        for j in range(i+1, n):
            collision = (i > j)
            collisions += collision * (n - i - 1) // 2

    return collisions
