

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
    wheel_rad = 1/2 * c_inv / car_mass
    h = lane_distance + wheel_rad * 2
    mu = car_mass / n
    road_system = h * (mu + 1)
    num_collisions = (2 * n - 1) * (road_system - 1)
    return num_collisions

