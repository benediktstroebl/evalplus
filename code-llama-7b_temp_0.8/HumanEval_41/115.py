

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
    # initialise to 0
    num_collisions = 0

    # setup cars
    cars_left = [0] * n
    cars_right = [0] * n
    for i in range(n):
        cars_left[i] = 2 * i
        cars_right[i] = 2 * n - 1 - i

    # Find the collision points
    collisions = []
    for i in range(n):
        for j in range(n):
            if cars_left[i] > cars_right[j]:
                collisions.append((cars_left[i], cars_right[j]))
            else:
                collisions.append((cars_right[j], cars_left[i]))

    # count collisions
    num_collisions = len(collisions)

    return num_collisions

