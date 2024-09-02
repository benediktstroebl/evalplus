

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

    assert n > 1

    car_race = [0] * 2 * n
    for i in range(2 * n):
        if (i % 2 == 0):
            car_race[i] = 1
        else:
            car_race[i] = -1

    index = 0
    collision_count = 0
    while (index < 2 * n):
        for i in range(index, index + 2 * n):
            if (car_race[i] == 1 and car_race[index] == 1):
                collision_count += 1
        index += 1
    return collision_count

