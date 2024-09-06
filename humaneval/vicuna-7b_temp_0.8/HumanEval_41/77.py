

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
    # Set up the initial positions of the cars
    positions = [(i+1, i+2) for i in range(n)]
    # Initialize a counter to keep track of the number of collisions
    collision_count = 0
    # Iterate over each pair of cars (i, j)
    for i in range(1, n):
        for j in range(i+1, n):
            # Check if the car at position (i, j) has hit a car at a different position
            if positions[i][0] == positions[j][1]:
                collision_count += 1
    return collision_count
