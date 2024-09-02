

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
    # The number of cars that are moving left to right and the number of cars that are moving
    # right to left are the same, so we'll call this total_cars.
    total_cars = n

    # We'll start by counting the number of cars that are more than total_cars/2 units away
    # from the left edge of the road.  We'll do this by creating two sets of variables:
    # one set for the cars that are moving left to right and one set for the cars that are moving
    # right to left.
    left_cars = []
    right_cars = []

    for i in range(total_cars):
        if i < n//2:
            left_cars.append(i)
        else:
            right_cars.append(i)

    # We'll iterate over the cars that are more than total_cars/2 units away from the left edge
    # of the road and count the number of cars that are in the same row.
    # If a car is in the same row as another car, they'll collide.
    collision_count = 0
    for i in left_cars:
        for j in range(total_cars):
            if (i-j >= total_cars//2) and (i-j < total_cars):
                collision_count += 1

    return collision_count