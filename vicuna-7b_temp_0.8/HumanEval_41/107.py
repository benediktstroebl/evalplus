

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
    if n < 2:
        return 0
    # the number of collision
    collision = 0
    # n/2 cars are moving right to left
    cars_right_to_left = (n // 2, n // 2)
    # n/2 cars are moving left to right
    cars_left_to_right = (n // 2, n // 2)
    for i in range(cars_right_to_left[0], n - 1, n // 2):
        for j in range(cars_left_to_right[0], n - 1, n // 2):
            if i not in cars_right_to_left and j not in cars_left_to_right:
                collision += 1
    return collision