

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
    # We'll use the following variables to keep track of the positions of cars
    left_start = [0] * n
    right_start = [0] * n

    # Set the initial positions of the cars
    for i in range(n):
        left_start[i] = i
        right_start[i] = n + i

    # Increment the positions of the cars
    for i in range(n):
        for j in range(i, n):
            left_start[i] += 1
            right_start[j] -= 1

    # Initialize a counter for the number of collisions
    collision_count = 0

    # While there are still cars on the road...
    while n > 0:

        # ... check for collisions
        for i in range(n):
            if left_start[i] == right_start[i]:
                collision_count += 1
    
        # Decrement the number of cars on the road
        n -= 1

    return collision_count