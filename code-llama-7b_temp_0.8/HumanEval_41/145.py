

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
    # Use Dynamic programming:
    # dp[i] is the number of collision if the i'th car is moving left to right
    # dp[n + 1 - i] is the number of collision if the i'th car is moving right to left
    # The answer is the sum of all dp[i] values

    # Initialize dp
    dp = [0 for _ in range(n + 1)]

    # Do DP
    for i in range(1, n + 1):
        # If the i'th car is moving left to right
        dp[i] += dp[i - 1]

        # If the i'th car is moving right to left
        dp[n + 1 - i] += dp[n + 1 - i - 1]

    # return the sum of all dp[i] values
    return sum(dp)

