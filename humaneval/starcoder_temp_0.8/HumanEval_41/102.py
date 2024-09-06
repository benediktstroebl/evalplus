

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

    cars = [Car(LEFT, 1), Car(RIGHT, 1)]
    cars[1].direction = LEFT
    car_distance = 1
    count = 0

    for _ in range(n):
        for car in cars:
            car.move(car_distance)
            if car.collides(cars[(car.index + 1) % 2]):
                count += 1

    return count
