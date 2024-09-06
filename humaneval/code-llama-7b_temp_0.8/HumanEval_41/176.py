

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
    assert n > 0

    count = 0

    for i in range(1, n + 1):
        # calculate how many cars on the left and right
        left_cars = n
        right_cars = n

        while left_cars >= i:
            left_cars -= 1
            count += 1

        while right_cars >= i:
            right_cars -= 1
            count += 1

    return count
