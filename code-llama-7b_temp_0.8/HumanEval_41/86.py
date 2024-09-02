

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
    #
    # Note that the question is equivalent to:
    #   What is the total number of cars?
    #   What is the number of cars that will hit cars on their left?
    #
    #  Cars are moving left to right, but they all start out at the same spot,
    #  and then move at the same speed.  So if we say the leftmost car is at position x,
    #  then all other cars are at position x + 1, x + 2, ..., x + n.
    #  The leftmost car will hit the car on its left after n steps.
    #  The car on its left will hit the car on its left after n - 1 steps.
    #  The car on its left will hit the car on its left after n - 2 steps.
    #  The car on its left will hit the car on its left after n - 3 steps.
    #  And so on.  The total number of collisions is
    #  n + n - 1 + n - 2 + ... + 3 + 2 + 1
    #  which is simply
    #  n * (n + 1) / 2
    return n * (n + 1) // 2
