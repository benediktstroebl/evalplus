

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
    if n == 0:
        return 0

    # Divide the n cars into two sets of n cars.
    # Each set of cars will contain cars moving in the direction of
    # left to right or right to left.
    # (Note that we can't split the cars into three sets because
    #  when cars moving in the same direction collide with each other,
    #  they will reverse their direction and keep moving.)

    # In order to count the number of collisions, the cars in the left to right
    # set of cars need to pass through the cars in the right to left set of cars.
    # Therefore, the cars in the left to right set should move faster than the cars
    # in the right to left set.
    # If the cars in the left to right set of cars move at a speed of s, and
    # the cars in the right to left set of cars move at a speed of (1-s),
    # the number of collisions will be equal to (s*(s+1))/2.

    return (n * (n+1)) // 2

