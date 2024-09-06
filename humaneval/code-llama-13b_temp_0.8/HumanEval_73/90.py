
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
    if len(arr) < 2:
        return 0
    n = len(arr)

    # dp[i][j] represents the minimum number of operations needed to make the subarray from index i to j
    # (both inclusive) palindromic. We can convert this 2D problem to a 1D problem by flattening it.
    dp = [float("inf") for _ in range(n * n)]
    for i in range(n):
        dp[i * n + i] = 0

    for i in range(n):
        for j in range(i - 1, -1, -1):
            dp[j * n + i] = min(
                dp[j * n + i], dp[(j + 1) * n + i] + 1
            )  # dp[(j + 1) * n + i] + 1 = number of operations to make arr[j+1:i+1] palindromic
            if arr[j] == arr[i]:
                dp[j * n + i] = min(dp[j * n + i], dp[j * n + (i - 1)])

    return min(dp[i * n + n - 1] for i in range(n))

