

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
    def time_to_collide(car_1: int, car_2: int):
        """
        return the time it takes for the two cars to collide
        """
        if car_1 % n == car_2 % n == 0:
            return 0
        elif car_1 % n > car_2 % n:
            return car_1//n
        else:
            return car_2//n

    cc = 0
    for i in range(n):
        for j in range(i):
            car_1, car_2 = i, j
            if time_to_collide(car_1, car_2) > 0:
                cc += 1

    return cc

