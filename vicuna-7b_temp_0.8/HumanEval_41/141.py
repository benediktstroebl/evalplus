

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
    # Create an empty list to store the number of collisions
    collisions = []
    # Set the number of cars for each direction
    cars_left = [i for i in range(n)]
    cars_right = [i for i in range(n)]

    # Iterate through the cars in the left direction
    for i in range(n):
        # Check if the car has reached the rightmost position
        if i == n - 1:
            # Iterate through the cars in the right direction
            for j in range(n):
                # Check if the car has reached the leftmost position
                if j == 0:
                    # If both cars are at the same position, they collide
                    collisions.append(1)
                    
    # Iterate through the cars in the right direction
    for j in reversed(range(n)):
        # Check if the car has reached the leftmost position
        if j == 0:
            # If both cars are at the same position, they collide
            collisions.append(1)
        # Iterate through the cars in the left direction
        for i in reversed(range(n)):
            # Check if the car has reached the rightmost position
            if i == n - 1:
                # If both cars are at the same position, they collide
                collisions.append(1)
    # Return the number of collisions
    return len(collisions)