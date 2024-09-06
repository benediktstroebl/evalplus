

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
    # Calculate the time at which the two sets of cars will meet.
    t1 = time_of_collision(n_left, v_left)
    t2 = time_of_collision(n_right, v_right)
    tdiff = abs(t2 - t1)
    # Calculate the speed of the cars at the moment of collision.
    v_collision = (v_left + v_right) / 2
    # Calculate the number of cars that collide
    n_collision = tdiff * v_collision
    return n_collision
