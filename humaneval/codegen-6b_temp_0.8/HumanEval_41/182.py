

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
    cars = {'left': [], 'right': []}
    for i in range(n):
        cars['left'].append(Car('left'))
        cars['right'].append(Car('right'))
    for i in range(n):
        cars['left'][i].move(1)
        cars['right'][i].move(1)
    collisions = 0
    while len(cars['left']) > 0 and len(cars['right']) > 0:
        if cars['left'][0].get_next_position()[0] > cars['right'][0].get_next_position()[0]:
            cars['right'].pop(0)
            collisions += 1
        else:
            cars['left'].pop(0)
            collisions += 1
    return collisions
