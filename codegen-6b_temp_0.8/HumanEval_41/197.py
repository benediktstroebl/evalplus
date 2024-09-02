

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
    import random
    car_count, car_speed = n, max(.1, random.random())
    col_count = 0

    while car_count > 1:
        for i in range(car_count):
            if car_speed <= .1:
                car_speed += random.random()
            if random.randint(0,1) == 0:
                car_count -= 1
            else:
                car_speed -= random.random()
        col_count += 1

    return col_count

