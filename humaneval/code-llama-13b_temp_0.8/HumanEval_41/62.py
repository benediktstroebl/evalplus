

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
    cars_left_right = cars_right_left = 0
    collisions = 0
    for i in range(1, n+1):
        if cars_right_left == i:
            cars_right_left = 0
        else:
            cars_right_left += i
        if cars_left_right == i:
            cars_left_right = 0
        else:
            cars_left_right += i
        collisions += cars_right_left // i

    return collisions

