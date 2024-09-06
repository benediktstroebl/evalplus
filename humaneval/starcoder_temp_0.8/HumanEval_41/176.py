

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
    cars = [(2*n, 2*n), (2*n, 2*n)]
    min_x, max_x = 0, 2*n
    speed = 1
    while min_x < max_x:
        if cars[0][0] < cars[1][0]:
            cars[0] = (cars[0][0] + speed, cars[0][1])
            min_x += 1
        else:
            cars[1] = (cars[1][0] - speed, cars[1][1])
            max_x -= 1
    return cars[0][1] < cars[1][1]
