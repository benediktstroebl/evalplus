
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
    n = len(arr)
    if n == 1:
        return 0
    dp = [[0] * (n + 1) for _ in range(n)]
    dp[0][0] = arr[0]
    dp[0][n] = arr[0]
    for i in range(1, n):
        dp[i][i] = arr[i]
        for j in range(1, n):
            dp[i][j] = (arr[i] + dp[j-1][j-1]) % n
    return dp[-1][-1]
