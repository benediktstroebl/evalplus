

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
    # A list of n/2 integers representing the starting positions of the cars.
    # It's guaranteed that the first half of the list starts with 0, and the second half starts with 1.
    positions = [0] * n // 2 + [1] * n // 2

    # A list of n/2 integers representing the velocities of the cars.
    # It's guaranteed that the first half of the list starts with 0, and the second half starts with 1.
    velocities = [0] * n // 2 + [1] * n // 2

    # A list of n/2 integers representing the trajectory of the left-moving cars.
    # It's guaranteed that the first half of the list starts with 0, and the second half starts with 1.
    left_trajectories = [0] * n // 2 + [1] * n // 2

    # A list of n/2 integers representing the trajectory of the right-moving cars.
    # It's guaranteed that the first half of the list starts with 0, and the second half starts with 1.
    right_trajectories = [0] * n // 2 + [1] * n // 2

    # A list of n/2 integers representing the status of the collision between cars.
    # It's guaranteed that the first half of the list starts with 0, and the second half starts with 1.
    collision_status = [0] * n // 2 + [1] * n // 2

    # Initialize the collision status list to 0.
    for i in range(n // 2):
        collision_status[i] = 0

    # The number of collisions.
    num_collisions = 0

    # The first half of the cars are moving right to left.
    for i in range(n // 2, -1, -1):
        # The second half of the cars are moving left to right.
        for j in range(n // 2, -1, -1):
            # Check if the two cars collide.
            if positions[i] == positions[j] and velocities[i] == velocities
