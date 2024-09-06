

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

    if n <= 0:
        return 0
    collision = 0
    car_left = []
    car_right = []
    car_left.append(n)
    car_right.append(n)
    while len(car_left) > 0:
        if len(car_left) > 1:
            car_left.append(car_left.pop() - 1)
        if len(car_right) > 1:
            car_right.append(car_right.pop() - 1)
        if len(car_left) > 0 and len(car_right) > 0 and car_left[0] <= 0 and car_right[0] <= 0:
            if car_left[0] <= 0:
                car_left.pop(0)
            if car_right[0] <= 0:
                car_right.pop(0)
            collision += 1
            if len(car_left) > 0 and len(car_right) > 0:
                car_left.append(car_left.pop() - 1)
                car_right.append(car
