
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
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    # dp[i][j] 表示将 arr[i:j] 变成回文需要的最小修改次数
    for l in range(n):
        for i in range(n - l):
            j = i + l
            if i == j:
                dp[i][j] = 0
            elif arr[i] == arr[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
    return dp[0][n - 1]
