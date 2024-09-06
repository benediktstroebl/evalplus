

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

    cars_left = [i for i in range(n, 0, -1)]
    cars_right = [i for i in range(1, n + 1)]

    count = 0
    while cars_left and cars_right:
        current_left_car = cars_left.pop(0)
        current_right_car = cars_right.pop(0)
        if current_left_car > current_right_car:
            count += 1

    return count

