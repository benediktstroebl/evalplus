

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
    cars = [Car(C) for C in range(n)]
    for reading in range(n):
        for other in range(reading+1, n):
            if cars[reading].distance(cars[other]) <= Car.max_distance:
                cars[reading].collide(cars[other])
    assert all(0 <= C.distance(C) <= Car.max_distance for C in cars)
    return sum(C.out_of_bounds for C in cars)

