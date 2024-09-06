

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
    # Our new car that we're going to be testing
    car = Car(0, 0, 0)

    # A line of cars moving left to right
    cars = [Car(i, car.y, car.x) for i in range(n)]

    # And a line of cars moving right to left
    cars += [Car(n - i - 1, car.y, car.x) for i in range(n)]

    # Some initialisations
    collisions = 0

    # Loop through all the cars
    for i in range(n):
        for j in range(i + 1, n):
            # Move cars left to right
            if (cars[i].x, cars[i].y) == (cars[j].x, cars[j].y):
                # encounter!
                collisions += 1
            elif (cars[i].x, cars[i].y) > (cars[j].x, cars[j].y):
                # move them to the left
                cars[j].x -= 1
            else:
                # move them to the right
                cars[i].x += 1

    return collisions
