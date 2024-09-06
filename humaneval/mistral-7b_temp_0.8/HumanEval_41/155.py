

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
    car_list = [0] * (2 * n)
    for i in range(n):
        car_list[i] = i + 1
        car_list[n + i] = i + 1

    car_pos = [0] * n
    car_speed = [1] * n

    for _ in range(2 * n - 1):
        for i in range(n):
            car_pos[i] += car_speed[i]
            if car_pos[i] == n - 1:
                car_pos[i] = 0
            if car_pos[i] == n:
                car_pos[i] = 0
                car_speed[i] *= -1
            if car_pos[i] == n - 1:
                car_pos[i] = 0
                car_speed[i] *= -1

        for i in range(n):
            car_pos[i] += car_speed[i]
            if car_pos[i] == n - 1:
