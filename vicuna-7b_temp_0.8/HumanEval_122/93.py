
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
    n = len(arr)
    if n < k:
        return 0
    dp = [0] * (n+1)
    dp[1] = arr[1]
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + (arr[i] - dp[i-2])) % 10
    return dp[k]
