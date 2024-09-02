

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
    assert n >= 1
    cars = ['L', 'R']
    cars_right = deque()
    cars_left = deque()
    collisions = 0

    for i in range(n):
        if i % 2 == 0:
            cars_right.append(cars.pop(0))
        else:
            cars_left.append(cars.pop(0))

    while cars_left and cars_right:
        if cars_left[0] == cars_right[0]:
            collisions += 1
            cars_left.popleft()
            cars_right.pop()
        else:
            if cars_left[0] == 'L':
                cars_left.append(cars_right.popleft())
            else:
                cars_right.append(cars_left.popleft())

    return collisions
