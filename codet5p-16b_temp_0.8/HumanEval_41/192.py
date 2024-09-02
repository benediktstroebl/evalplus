

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

    if n <= 0: return 0
    print(f"car_race_collision({n})")

    # We'll start by assuming that there are no collisions
    num_collisions = 0

    # If n is even, then every n // 2 cars move right
    if n % 2 == 0:
        n_right = n // 2
        n_left = n // 2
    else:
        n_right = n // 2 + 1
        n_left = n // 2

    # If there are no collisions, then the two cars will start moving towards
    # each other at the same speed, but in opposite directions
    if n_left > n_right:
        return num_collisions

    for i in range(n_left):
        # n_left cars are moving left to right
        car_left = (n_left - 1) - i
        car_right = (n_right - 1) - i

        # They're moving in the same speed; check if they collide
        if (car_left + 1) % (n_left - 1) == 0 and (car_right + 1
