

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
    # D: return type is a little tricky, because it could be either an integer or a float.
    # O(log(n))
    # Time to crash is 2n * log(n) / (n + 1)
    # Length of time is T, time to crash is t
    # T = t * (n + 1) / 2n
    # t = 2T / (n + 1)
    # O(2T / (n + 1)) = O(log(n))
    # n = 2**k
    # T = 2**(k + 1) * log(2) * log(k + 1)
    #
    # Better:
    # O(n) + O(log(n))
    #
    # 1.  Compute the first car in the left-moving cars to collide with the first car in the
    #     right-moving cars.   The left-moving car that collides first has the same index as
    #     the right-moving car.  Let this left-moving car be #i.
    #
    # 2.  Compute the first car in the left-moving cars to collide with the i-th right-moving
    #     car.  Let this left-moving car be #j.
    #
    # 3.  Compute the first car in the left-moving cars to collide with the j-th right-moving
    #     car.  Let this left-moving car be #k.
    #
    # 4.  Compute the first car in the left-moving cars to collide with the k-th right-moving
    #     car.  Let this left-moving car be #l.
    #
    # 5.  Repeat step 4 until l is less than or equal to i.
    #
    #     We're done when l is equal to i.
    #
    #     We're done before l is less than i if and only if the j-th right-moving car collides
    #     with at least one left-moving car.
    #
    #     To
