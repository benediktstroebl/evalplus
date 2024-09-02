

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
    # Initialize variables
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    cars_left = [True for i in range(n)]
    cars_right = [True for i in range(n)]
    collisions = 0

    # Sort the cars by their indices
    while len(left_cars) > 1:
        _, j = min(left_cars, key=lambda x: x // 2)
        _, i = max(left_cars, key=lambda x: x // 2)
        left_cars.remove(j)
        left_cars.insert(i, j)

    while len(right_cars) > 1:
        _, j = min(right_cars, key=lambda x: x // 2 + n)
        _, i = max(right_cars, key=lambda x: x // 2 + n)
        right_cars.remove(j)
        right_cars.insert(i, j)

    # Check for collisions between cars moving left to right
    for i in range(n):
        if not cars_left[i]:
            for j in range(i, n):
                if cars_right[j]:
                    collisions += 1

    # Check for collisions between cars moving right to left
    for i in range(n):
        if not cars_right[i]:
            for j in range(i, n):
                if cars_left[j]:
                    collisions += 1

    return collisions