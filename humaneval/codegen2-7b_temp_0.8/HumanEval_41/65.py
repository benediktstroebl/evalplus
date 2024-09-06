

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
    _, collisions = 0, 0
    for _ in range(n):
        curr_cars, next_cars = deque(), deque()
        for _ in range(2):
            for car in curr_cars:
                if car > 0:
                    break
            else:
                curr_cars.append(2)
            for car in curr_cars[::-1]:
                if car > 0:
                    break
            else:
                curr_cars.append(-1)
            next_cars.append(car)
            collisions += 1
    return collisions
