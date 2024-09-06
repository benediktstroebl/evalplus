
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

    def is_palindromic(arr):
        return arr == arr[::-1]

    arr = sorted(arr)
    N = len(arr)
    dp = [[1000000 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 0

    for i in range(N):
        dp[i][i] = 0

    for i in range(N - 1):
        if is_palindromic(arr[:i + 1]):
            dp[0][i + 1] = 0
        if is_palindromic(arr[i + 1:]):
            dp[i + 1][N - 1] = 0

    for i in range(1, N):
        for j in range(i + 1, N):
            if arr[i - 1]!= arr[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)

    return dp[-1][-1]

