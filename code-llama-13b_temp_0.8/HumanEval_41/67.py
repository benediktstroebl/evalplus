

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

    def distance(p: int):
        return (n - p) + p

    def expected_num_of_collisions(k: int):
        """
        k is a number in the range 0 .. (n-1)
        This function computes the expected number of collisions
        that will happen as we traverse the two sets of cars,
        when the first car that is considered collides with car number k
        """

        #
        # This is the expected number of collisions that will happen
        # as we traverse the two sets of cars, when the first car
        # that is considered collides with car number k
        #
        # The first car is car p, which starts at position 0, and travels at speed 1
        #   to position n
        #
        # The kth car is car k, which starts at position k and travels at speed -k
        #   to position -k
        #
        # The total distance traveled by the first car is n
        # The total distance traveled by the kth car is 0
        #
        # If the two cars do not collide, the cars will
        # never have a collision, since the kth car moves in the opposite
        # direction as the first car
        #
        # If the two cars do collide, the cars will collide k times
        #
        #
        # We will divide this function into three cases, depending on which of
        # the two cars that we are considering moves first.
        #
        #
        # Case 1:  The first car to move starts at position 0
        # ---------------------------------------------------
        #
        # If the first car moves first, then the cars do not collide.
        #
        # We do not care what the second car does.
        #
        #
        # Case 2:  The second car to move starts at position k
        # ----------------------------------------------------
        #
        # If the second car moves first, then the cars do not collide
        #
        # We do not care what the first car does
        #
        #
        # Case 3:  The first car to move starts at position 1, and the second car
