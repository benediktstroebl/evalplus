

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

    # Your code goes below here
    car_speed = 0
    car_position = 0

    collision_count = 0

    while collision_count <= n:
        for i in range(n):
            car_speed += 1

            if i == 0:
                car_position += 1
            elif i == 1:
                car_position += 1
            elif i == 2:
                car_position += 1
            elif i == 3:
                car_position += 1
            elif i == 4:
                car_position += 1
            elif i == 5:
                car_position += 1
            elif i == 6:
                car_position += 1
            elif i == 7:
                car_position += 1
            elif i == 8:
                car_position += 1
            elif i == 9:
                car_position += 1
            elif i == 10:
                car_position += 1
            elif i == 1
