

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

    # track: (car_n, position, direction)
    cars = []
    for i in range(n):
        cars.append((i, 0, 1))
        cars.append((i, 1, -1))

    # sort by position
    cars.sort(key=lambda x: x[1])

    count = 0
    i = 0
    while i < len(cars):
        car_a, _, direction_a = cars[i]
        car_b, _, direction_b = cars[i+1]
        # i = index of car_a
        # i+1 = index of car_b
        # direction_a = -1 for car_a moving right to left
        # direction_b = 1 for car_b moving left to right

        if direction_a == direction_b:
            # they collide
            count += 1
        elif direction_b == -1:
            # car_b is ahead of car_a, meaning car_b is moving left to right
            # this means that car_a will collide with car_b in the future
            # therefore, we remove car_b
            cars.pop(i)
            cars.pop(i)
            # we decrement the index, since we removed two elements
            i -= 1
        else:
            # car_b is behind car_a, meaning car_b is moving right to left
            # therefore, we remove car_a
            cars.pop(i)
            cars.pop(i)
            i -= 1

        i += 1

    return count

