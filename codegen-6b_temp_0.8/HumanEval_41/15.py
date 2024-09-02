

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
    # def move(cars, direction):
    #     next_cars = []
    #     for car in cars:
    #         if direction == 'left':
    #             car.x -= 1
    #         elif direction == 'right':
    #             car.x += 1
    #         next_cars.append(car)
    #     return next_cars

    def move(cars, direction):
        if direction == 'left':
            for i in range(len(cars)):
                cars[i].x -= 1
        elif direction == 'right':
            for i in range(len(cars)):
                cars[i].x += 1

    cars_left = [Car() for i in range(n)]
    cars_right = [Car() for i in range(n)]

    for i in range(n):
        move(cars_left, 'left')
        move(cars_right, 'right')

    # while True:
    #     move(cars, 'left')
    #     move(cars, 'right')
    #     if max(c.x for c in cars) > 200:
    #         return

    return sum(min(c.x, 200 - c.x) for c in cars_left) + sum(max(c.x, 200 - c.x) for c in cars_right) - 2 * n

