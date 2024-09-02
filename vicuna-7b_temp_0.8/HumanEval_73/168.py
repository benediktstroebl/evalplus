
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
    dp = [[0] * (max(arr) + 1) for _ in arr]
    dp[0][0] = 1
    for i in range(1, len(arr)):
        for j in range(i, len(arr)):
            min_change = 0
            for k in range(i):
                for jj in range(j):
                    dp[i][jj] = min(dp[i][jj], dp[k][jj] + (arr[k][j] - arr[i][j]))
                min_change = min(min_change, dp[i][jj])
            dp[i][j] = min_change
    return dp[-1][-1]
