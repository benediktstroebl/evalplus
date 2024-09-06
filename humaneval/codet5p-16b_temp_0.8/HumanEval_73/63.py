
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
    dp = [[[float('inf')] * n for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i][i] = 0
    
    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            for k in range(i, j):
                if l == 1:
                    dp[i][j][k] = 0
                    continue
                cost = arr[i] ^ arr[k]
                dp[i][j][k] = min(dp[i][j][k], dp[i][k][k] + cost)
    
    return dp[0][n-1][n-1]

