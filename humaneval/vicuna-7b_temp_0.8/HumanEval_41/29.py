

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
    # Initialize variables
    cars = [0] * n
    d = {}
    for i in range(n):
        for j in range(i + 1, n):
            d[i, j] = 1
    cars[0] = 1  # first car
    cars[1] = 1  # second car

    # Find the number of collisions
    for i in range(2, n):
        for j in range(i + 1, n):
            if d[i-1, j-1] == 1 and d[i-1, j] == 0 and d[i, j-1] == 1:
                # There is a collision
                for k in range(i-1, j-1):
                    d[k, j] = d[k, j] - d[i-1, j] - d[i, j-1]
                for k in range(i, j+1):
                    d[k, j] = d[k, j] + d[i-1, j] + d[i, j-1]
                for k in range(j-1, i+1):
                    d[k, j] = d[k, j] + d[i, j-1] + d[i-1, j]
                # Update the number of cars
                cars[i] = cars[i] - 1
                cars[j] = cars[j] - 1

    return cars[0]
