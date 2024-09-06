

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
    # the total number of car pairs (n cars moving left to right + n cars moving right to left)
    total_pairs = 2*n

    # initialize the count of collisions
    collision_count = 0

    # loop through all possible car pairs
    for i in range(total_pairs):
        for j in range(i+1, total_pairs):
            # if the cars are not colliding, increment the count of collisions
            if i*n + j != j*n + i:
                collision_count += 1

    return collision_count
