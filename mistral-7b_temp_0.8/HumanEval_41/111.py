

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

    # Check if we've been given a valid input
    if n <= 0:
        return None

    # Now we've got our indexes, we can start computing the distances between each of
    # them
    distances = [0] * (2 * n)

    # We can compute the distances between each index to the left of us
    for i in range(1, n):
        distances[i] = distances[i-1] + i

    # We can compute the distances between each index to the right of us
    for i in range(1, n):
        distances[n+i-1] = distances[n+i-2] + i

    # We can now loop through each index and add all the distances between each
    # index to the left and the right of us to count the collisions
    collision_count = 0
    for i in range(n):
        collision_count += distances[i] + distances[i+n]

    return collision_count


