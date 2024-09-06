

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

    # The distance of car i from the beginning of the road.
    left = [0] * n
    # The distance of car i from the end of the road.
    right = [0] * n
    cars_moving_left = set()
    cars_moving_right = set()
    collisions = 0

    for i in range(n):
        left[i] = int(input())
    for i in range(n):
        right[i] = int(input())

    for i in range(n):
        if i in cars_moving_right:
            if right[i] >= left[i]:
                collisions += 1
            cars_moving_left.remove(i)
        else:
            if left[i] >= right[i]:
                collisions += 1
            cars_moving_right.add(i)

    return collisions
