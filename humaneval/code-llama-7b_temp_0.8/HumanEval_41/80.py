

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
    # number of collisions
    n_collisions = 0
    # # of times each car has passed the middle
    n_passed_middle = [0] * n
    # car position
    car_pos = [0] * n
    car_speed = [1] * n
    while True:
        for car in range(n):
            car_pos[car] += car_speed[car]
            if car_pos[car] >= n:
                n_passed_middle[car] += 1
                car_pos[car] = n
        for car in range(n):
            car_speed[car] -= 1
            if n_passed_middle[car] >= n:
                n_collisions += 1
                return n_collisions
        if car_pos[car] <= 0:
            n_passed_middle[car] += 1
            car_pos[car] = 0

