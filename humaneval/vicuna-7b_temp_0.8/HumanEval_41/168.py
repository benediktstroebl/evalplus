

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
    # A007848
    # The number of ways to move n cars in the left-to-right direction,
    # assuming they all start at the same position and move at the same speed
    # (and there are no collisions) is given by the Catalan numbers:
    # C(n+1, 1) = n+1, C(n+2, 2) = n+2, C(n+3, 3) = n+3, ...
    # (A001048)
    # The number of ways to move n cars in the right-to-left direction,
    # assuming they all start at the same position and move at the same speed
    # (and there are no collisions) is given by the Catalan numbers:
    # C(n+1, -1) = n+1, C(n+2, -2) = n+2, C(n+3, -3) = n+3, ...
    # (A001049)

    # In this case, we are interested in the number of collisions
    # that occur when the two sets of cars meet.
    # We can count the number of ways to choose which set of cars
    # is moving left-to-right, and then multiply by the total number
    # of ways to move n cars in that direction.
    # We can do the same for the set of cars moving right-to-left.
    # Finally, we add the two results together.
    # Note that we are not counting collisions where a car moving left-to-right
    # hits a car moving right-to-left, because those are already counted above.
    return sum(C(n+1, 1) * C(n+1, -1) for _ in range(n))