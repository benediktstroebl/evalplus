
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

    # 1. Initialize dp[i][j] to +inf
    dp = [[float("inf")] * n for _ in range(n)]

    # 2. dp[i][i] = 0
    for i in range(n):
        dp[i][i] = 0

    # 3. For each i, fill the arr[i][i+1], arr[i+1][i+2]... up to arr[n-1][n-1]
    for diff in range(1, n):
        for i in range(n - diff):
            # If the first and last elements are same, then no need to change any element
            if arr[i] == arr[i + diff]:
                dp[i][i + diff] = 0
            else:
                # Minimum of, change the first element to second element, change the second element
                # to first element, or change the middle two elements
                dp[i][i + diff] = 1 + min(
                    dp[i + 1][i + diff], dp[i][i + diff - 1], dp[i + 1][i + diff - 1]
                )

    return dp[0][n - 1]

