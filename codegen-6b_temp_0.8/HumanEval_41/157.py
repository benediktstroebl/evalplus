

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
    cars = [Car(i) for i in range(0, n)]
    count = 0
    while True:
        for car in cars:
            car.move()
        for car in reversed(cars):
            car.move()
        for car in cars:
            if car.distance < 0:
                cars.remove(car)
            if car.distance > 0:
                count += 1

        if len(cars) == 1:
            break
    return count

