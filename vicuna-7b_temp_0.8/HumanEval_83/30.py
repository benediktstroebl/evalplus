
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # This function uses dynamic programming to count the number of 1-power
    # numbers that start or end with 1.

    # We start by counting the number of 1-power numbers that start with 1
    # and end with 1. If the number is odd, there is only 1 such number,
    # which is 1 itself. If the number is even, there are 2 such numbers:
    # 1 and 10.
    dp = [[0] * (n+1) for _ in range(n+1)]

    # We then use the dp array to count the number of 1-power numbers that
    # start with 1 and end with 1 by filling in the rest of the array.
    # We start with the first row, which represents the number of 1-power
    # numbers that start with 1 and end with 1. The first cell is 1, and
    # the rest are 0s. Then, we fill in the rest of the array by summing
    # the cells in the current row and the next row. The cells in the next
    # row represent the number of 1-power numbers that start with 1 and
    # end with 1, where the last digit is 0.

    # We continue this process until we have filled in the entire dp array.

    # Finally, we return the value of dp[n][n-1], which is the number of
    # 1-power numbers that start or end with 1.

    return dp[n][n-1]
