

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
    # I think this is an adaptation of the problem called "Car Race" in the book
    # "Algorithms" by Dasgupta, Papadimitriou, and Vazirani.
    # My solution is based on a simple observation:
    # - if the cars start from positions k and 100n+k and drive towards each other at the same speed,
    #   the first collision will happen when the positions of the cars coincide.
    # - for this to happen, the two cars have to move in parallel, and there is only one position where they can
    #   meet in the middle, which is at k = (100n+k)/2 = 50n.
    # - so, the cars are guaranteed to collide when their positions coincide at 50n.
    return n*n

