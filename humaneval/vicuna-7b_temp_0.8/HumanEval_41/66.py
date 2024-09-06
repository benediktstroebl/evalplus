

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
    # The total distance that the cars have traveled
    total_distance = 0

    # The positions of the cars at time t
    positions = [[0] * n for _ in range(n)]

    # The speeds of the cars
    speeds = [1] * n

    # We are keeping track of the number of collisions
    collisions = 0

    # We are keeping track of the total distance traveled
    for t in range(n // 2):
        # Compute the position of the cars at time t
        positions[0][t] = t

        # Compute the speed of the cars at time t
        # The speed of the cars is always 1
        speeds[0][t] = 1

        # Update the total distance traveled
        total_distance += 1

        # The rest of the positions and speeds are computed recursively
        car_race_collision(n // 2, positions, speeds, total_distance, collisions)

    return collisions
