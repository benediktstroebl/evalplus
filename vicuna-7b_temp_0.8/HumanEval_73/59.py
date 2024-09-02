
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
    dp = [[1e9] * (n + 1) for _ in range(n)]
    for i in range(n):
        dp[0][i] = arr[i]
    for i in range(1, n):
        for j in range(i):
            for k in range(i, n):
                if j != k:
                    dp[j][i] = min(dp[j][i], dp[k][j])
                else:
                    dp[j][i] = min(dp[j][i], dp[i][k])
    return dp[-1][-1]
