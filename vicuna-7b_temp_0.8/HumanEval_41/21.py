

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
    car1 = 2 ** n
    car2 = car1 // 2

    # calculate the distances
    left_distance = car1 // 2 + car2
    right_distance = car1 // 2 + car2 * 2

    # check the collisions
    for i in range(left_distance):
        if left_distance - i < right_distance:
            return 0

    for i in range(right_distance):
        if left_distance - i < right_distance:
            return 0

    # check the rest of the distance
    for i in range(left_distance, car1 - left_distance):
        if left_distance - i < right_distance:
            return 0

    for i in range(right_distance, car1 - right_distance):
        if left_distance - i < right_distance:
            return 0

    return 1