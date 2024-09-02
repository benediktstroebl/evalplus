

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
    # We can brute force this problem and check for every possible sequence of cars.
    # That's going to take O(2^n).

    # We can also solve this problem in O(n) time.  (The intuition here is that we should
    # see collisions when two cars that have been moving in opposing directions get very
    # close together.)
    #
    # We'll make two arrays; one for cars moving right to left, and one for cars moving left to right.
    # Initially, the two arrays have n elements, each initialized to 0.
    # We'll iterate through the cars from left to right.  For each car, if the car is moving right to
    # left, then we'll decrement the value in the left-to-right array corresponding to that car's
    # position.  If the car is moving left to right, then we'll decrement the value in the right-to-left
    # array corresponding to that car's position.
    #
    # The point of this is that as we move through the cars from left to right, each car's position
    # has a corresponding value in one of the arrays, which will be negative if the car is moving
    # left to right and positive if the car is moving right to left.  The two arrays will eventually
    # end up having the same values, indicating collisions.
    pass
