

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

    # Time: O(n log n)
    # Space: O(1)
    # The algorithm below implements the solution for a case where both of the sets of cars
    # have the same speed.  The cars in set 1 move from left to right with the speed v, and
    # the cars in set 2 move from right to left with the speed -v.  Each collision adds 2v
    # to the final answer, so we can just do a single pass to compute the sum of v * (cars
    # moving from left to right) - v * (cars moving from right to left).
    #
    # We can improve the running time to O(n) by having two pointers p1 and p2 where p1
    # points to a car in set 1 and p2 points to a car in set 2.  We then increment p1
    # (and p2) until p1 reaches a car whose speed is <= v, and p2 until a car with speed
    # >= -v.  Then, the next collision will occur when p1 == p2.  We then continue to increment
    # p1 and p2, as long as p1 != p2, and we have not reached the end of both lists.
    # The above algorithm is applied on two sorted lists, one for cars moving from left to right,
    # and the other for cars moving from right to left.
    #
    # The total running time is O(n) + O(n) = O(n), and the total space complexity is O(1).
    return sum(v1 * v2 for v1, v2 in zip(left, right))

