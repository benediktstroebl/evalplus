

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

    cars_driving_left = set(range(1, n + 1))
    cars_driving_right = set(range(n, 0, -1))

    collisions = 0
    while cars_driving_left:
        car_1 = cars_driving_left.pop()
        car_2 = cars_driving_right.pop()
        if car_1 == car_2:
            collisions += 1
        else:
            cars_driving_right.add(car_2)
            cars_driving_left.add(car_1)

    return collisions

