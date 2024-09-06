

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
    cars = [Car() for _ in range(n)]
    collisions = 0
    while True:
        for car1 in cars:
            car1.move()

        cars = sorted(cars, key=lambda car: car.pos)
        for car2, car1 in zip(cars, cars[1:]):
            if car1.pos == car2.pos:
                collisions += 1
                car1.pos = 0
                car2.pos = 0

