

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

    # Compute all the possible collision locations
    # Colisions occur in 2k + 1 places, where k is the number of cars
    # 1. There are k + 1 possible collision points between cars 0 and k
    # 2. There are k + 1 collision points between cars k and 2k
    # 3. There are k collision points between cars k+1 and 2k-1
    # 4. There are k collision points between cars k+2 and 2k-2
    # ...
    # There are k + 1 collision points between cars n-k-1 and 2k - n + k + 1
    # There are k + 1 collision points between cars n-k and n

    collision_locations = []
    for i in range(0, n):
        if i == 0:
            collision_locations += [i, n - i - 1]
        else:
            collision_locations += [i, n - i - 1, n - i - 2]

    return collision_locations

