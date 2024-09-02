

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
    collision_count = 0

    # For each car
    for i in range(n // 2):
        # Find the position of the leftmost car
        left_start = i * (n + 1)

        # Find the position of the rightmost car
        right_start = (i + 1) * (n + 1)

        # Find the position of the middle car
        middle_start = (i + 0.5) * (n + 1)

        # For each car
        for j in range(n // 2):
            # If both cars are on the same position
            if middle_start <= right_start <= left_start and middle_start <= left_start <= right_start:
                # Collision detected
                collision_count += 1

    # Return the number of collisions
    return collision_count