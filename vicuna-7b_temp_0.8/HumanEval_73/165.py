
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    if not arr:
        return 0
    n = len(arr)
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[0][0] = 1
    dp[0][i] = dp[0][i-1] for i in range(2, n+1)
    for i in range(2, n):
        for j in range(i, n):
            if arr[i-1] != arr[j-1]:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = dp[i-1][j-1]
    return dp[n-1][0]
