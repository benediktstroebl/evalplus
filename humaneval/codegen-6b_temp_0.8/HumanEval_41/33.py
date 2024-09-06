

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
    cars_on_left = list(range(1, n + 1))
    cars_on_right = list(range(n, 0, -1))
    collisions = 0

    while True:
        if not cars_on_left:
            break
        if not cars_on_right:
            break

        if cars_on_left[0] > cars_on_right[0]:
            cars_on_left.pop(0)
            cars_on_right.pop(0)
            collisions += 1
        else:
            cars_on_left.pop(0)
            cars_on_right.pop()

    return collisions

