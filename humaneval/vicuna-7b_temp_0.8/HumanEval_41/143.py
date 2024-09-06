

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
    # n cars driving left to right, n cars driving right to left
    n_cars_left = n
    n_cars_right = n

    # number of collisions
    collisions = 0

    # checking if collisions happen
    for i in range(n_cars_left // 2):
        for j in range(i + 1, n_cars_left):
            for k in range(j + 1, n_cars_right):
                if (i - j) * (i - j) + (j - k) * (j - k) < 0:
                    collisions += 1

    return collisions