

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
    # As above, we create the universe of all possible trajectories in a 2D grid,
    # where each grid cell represents a trajectory of a car.
    # However, this time, we don't sort the trajectories by their starting position.
    # Instead, we sort them by the number of cars that are driving right to left,
    # because that determines the order in which the cars will collide.
    universe = generate_trajectory_universe(n)
    num_collisions = 0
    # We iterate through the grid of trajectories.
    for trajectory in universe:
        # For each trajectory, we check whether there is another trajectory that
        # overlaps with it and is moving in the opposite direction.
        # If there is, we increment the counter of collisions.
        for other_trajectory in universe:
            if (trajectory[0] == other_trajectory[0] and
                    trajectory[1] > other_trajectory[1] and
                    other_trajectory[1] > trajectory[1]):
                num_collisions += 1
    return num_collisions