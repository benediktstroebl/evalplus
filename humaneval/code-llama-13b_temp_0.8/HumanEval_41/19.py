

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
    if n == 1:
        return 0
    if n == 2:
        return 1

    # This is the maximum distance a car that's driving left to right can go before
    # hitting a car that's driving right to left.
    max_distance_ltr = 0
    # This is the maximum distance a car that's driving right to left can go before
    # hitting a car that's driving left to right.
    max_distance_rtl = 0

    # The distance a car has to travel to collide with a car traveling right to left
    distance_ltr = 0
    # The distance a car has to travel to collide with a car traveling left to right
    distance_rtl = 0

    # The number of collisions that happen in one go.
    collisions = 0

    # We'll use two cars to go through the entire range of numbers.  If the cars meet
    # or exceed each other, that means that there was a collision.
    for i in range(1, n + 1):
        max_distance_ltr += i
        distance_rtl = i

        for j in range(1, n + 1):
            max_distance_rtl += j
            distance_ltr = j

            # There's a collision if the distance between the cars is greater than or
            # equal to the maximum distance they can travel.
            if distance_ltr >= max_distance_rtl:
                collisions += 1

            if distance_rtl >= max_distance_ltr:
                collisions += 1

    return collisions

