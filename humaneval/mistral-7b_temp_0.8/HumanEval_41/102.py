

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
    cars = {(i, 1): -1 * i for i in range(1, n+1)}
    cars.update({(i, 2): i for i in range(1, n+1)})
    count = 0
    while cars:
        for k, v in cars.items():
            if cars[(v+k)[0], 1] != None and cars[(v+k)[1], 2] != None:
                if cars[(v+k)[0], 1] == cars[(v+k)[1], 2]:
                    count += 1
        for k, v in cars.items():
            if cars[(v+k)[0], 1] != None:
                cars[cars[(v+k)[0], 1]] = None
            if cars[(v+k)[1], 2] != None:
                cars[cars[(v+k)[1], 2]] = None
    return count
