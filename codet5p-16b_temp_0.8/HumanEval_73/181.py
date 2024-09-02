
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
    m = sum(arr) // 2
    dp = [[False for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] = True
                continue
            if j == 0:
                dp[i][j] = False
                continue
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return m - dp[n][m]

