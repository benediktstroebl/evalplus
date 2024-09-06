
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    n = len(arr)
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    dp[n-1] = arr[0]
    for i in range(2,n):
        if arr[i] <= arr[i-1]:
            dp[i] = dp[i-1]
        else:
            dp[i] = max(dp[i-1], arr[i] + dp[i-1])
    return dp[n-2]
