

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
    car_left = []
    car_right = []
    collisions = 0

    for i in range(n):
        car_left.append(0)
        car_right.append(0)

    for _ in range(100000):
        if car_left[0] > 0:
            car_left[0] -= 1
            if car_right[0] > 0:
                car_right[0] -= 1
                collisions += 1
        elif car_right[0] > 0:
            car_right[0] -= 1
            if car_left[0] > 0:
                car_left[0] -= 1
                collisions += 1
        else:
            for j in range(n-1):
                car_left[j] = car_left[j+1]
                car_right[j] = car_right[j+1]

    return collisions

