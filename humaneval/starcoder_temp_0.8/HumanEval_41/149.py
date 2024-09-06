

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

    # In the general case, we need to find the number of times that the cars intersect
    # with each other.  This is a bit of a complicated problem, though.  There are
    # two ways to approach it:
    #
    # 1.  We can start out with n=2.  This is a very simple case:  if we have two cars
    #     going left to right, then they'll collide if they're moving towards each
    #     other.  If we have two cars going right to left, then they'll collide
    #     if they're moving away from each other.
    #
    # 2.  We can start out with n=4.  If we have two cars going left to right, then
    #     they'll collide if they're moving towards each other.  If we have two cars
    #     going right to left, then they'll collide if they're moving away from each
    #     other.  We can divide up the case with n=4 into two cases:
    #      - the two cars going left to right
    #      - the two cars going right to left
    #     and then combine the results.
    #
    # Note that there are many possible combinations.  This approach gives the answer
    # for n=2, n=3, n=4, n=5, n=6, and n=7.  This approach gives the answer for n=4
    # and n=7.
    #
    # There are better ways to approach the problem.  For example, we can work in
    # the lower half of the numbers; e.g., find collisions for n=10.  Then, we can
    # use a similar method to work in the upper half of the numbers; e.g., find
    # collisions for n=9.  Then, we can combine the results.
    #
    # For example, we could work with n=20.  This gives an answer of 30, which is
    # the correct answer.  Then, we can work with n=21.  This gives an answer of
    # 31.  Then, we can work with n=19.  This gives an answer of 29.  Then, we can
    # combine the results.
    #
    # There are nine possible combinations of two numbers that are less than or equal
    #
