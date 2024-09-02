

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
    cars_going_left = [0 for i in range(n)]
    cars_going_right = [0 for i in range(n)]
    collisions = 0
    for i in range(n):
        cars_going_left[i] = i
    for i in range(n):
        cars_going_right[i] = n - 1 - i
    while len(cars_going_left) > 0 and len(cars_going_right) > 0:
        for i in range(len(cars_going_left)):
            cars_going_left[i] += 1
            if cars_going_left[i] == cars_going_right[0]:
                collisions += 1
                cars_going_left[i] = 0
                cars_going_right[0] = 0
                break
        for i in range(len(cars_going_right)):
            cars_going_right[i] -= 1
            if cars_going_left[0] == cars_going_right[i]:
              
