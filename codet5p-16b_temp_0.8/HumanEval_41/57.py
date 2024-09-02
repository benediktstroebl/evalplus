

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

    num_collisions = 0
    collisions_so_far = set()

    for i in range(n):
        if i % 2 == 0:
            car_x = 1
        else:
            car_x = -1

        for j in range(n):
            if j % 2 == 0:
                car_y = 1
            else:
                car_y = -1

            new_car_x = car_x + j
            new_car_y = car_y

            if (new_car_x, new_car_y) in collisions_so_far:
                num_collisions += 1
                break
            else:
                collisions_so_far.add((new_car_x, new_car_y))

    return num_collisions

