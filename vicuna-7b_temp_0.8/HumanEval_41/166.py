

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
    # Initialize empty list to store the numbers of collisions for each set of n cars
    collisions = [[0] * n for _ in range(n)]

    # Iterate through the first set of cars
    for i in range(n):
        collision = 0
        # Iterate through the second set of cars
        for j in range(n):
            if i + j < n:
                # If the two cars are on the same position
                if i + j == n:
                    collision = 1
                else:
                    # Otherwise, they collide
                    collision = 1

        # Increment the number of collisions for the first set of cars
        collisions[i][0] += collision

    # Iterate through the second set of cars
    for i in range(n):
        collision = 0
        # Iterate through the first set of cars
        for j in range(n):
            if i + j < n:
                # If the two cars are on the same position
                if i + j == n:
                    collision = 1
                else:
                    # Otherwise, they collide
                    collision = 1

        # Increment the number of collisions for the second set of cars
        collisions[j][0] += collision

    return sum(collisions[i][1] for i in range(n))