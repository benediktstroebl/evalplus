

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
    for i in range(n):
        car_1 = [0, 0]
        car_2 = [0, 0]
        x = 0
        y = 0
        for i in range(2 * n):
            x += 1
            y += 1
            if y > n:
                y = 1
                x = 0
        car_1 = [x, y]
        x = 0
        y = 0
        for i in range(2 * n):
            x += 1
            y += 1
            if y > n:
                y = 1
                x = 0
        car_2 = [x, y]
        print(car_1, car_
