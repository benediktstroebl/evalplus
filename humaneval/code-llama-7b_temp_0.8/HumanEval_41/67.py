

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

    # Efficiency is important here; the test data can be as large as 10,000
    # so we need to be efficient in space and time
    # So we will not store the whole array, only store the last 2 values to find
    # if there's a collision.
    # We will also use dynamic programming, by storing the answer to each
    # subproblem.

    # Create arrays to store answers to subproblems
    answer = [0] * n
    previous = [0] * n
    next = [0] * n

    # initialize first answer to 0, previous to 0, next to 0
    answer[0] = 0
    previous[0] = 0
    next[0] = 0

    # solve subproblems
    for i in range(1, n):
        # this car is moving left to right, so it's the next one
        next[i] = previous[i - 1]

        # this car is moving right to left, so it's the previous one
        previous[i] = next[i - 1]

        # increment answer to current subproblem
        answer[i] = next[i - 1] + previous[i]

    # return answer to entire problem
    return answer[-1]

