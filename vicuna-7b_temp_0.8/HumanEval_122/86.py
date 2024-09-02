
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    digits = [str(x) for x in arr]
    dp = [0] * (k+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, len(digits)):
        dp[i] = dp[i-1] + dp[i-2]
    for i in range(k+1):
        if len(digits[i]) <= 2:
            dp[i] += digits[i]
    return dp[k]
