
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
    # code goes here
    table = [[[float("inf")] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    dp = [[[float("inf")] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                table[i][j][k] = float("inf")
                dp[i][j][k] = float("inf")

    for i in range(n):
        table[i][i][0] = 0
        table[i][i][i + 1] = 0

    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 or i == j:
                continue
            else:
                if arr[i - 1] == arr[j - 1]:
                    table[i - 1][j - 1][i] = table[i - 1][j - 1][i - 1]
                else:
                    table[i - 1][j - 1][i] = min(
                        table[i - 1][j - 1][i - 1] + 1,
                        table[i - 1][j][i - 1] + 1,
                        table[i][j - 1][i - 1] + 1,
                    )

    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                dp[i][j][k] = min(
                    table[i][j][k],
                    dp[i][k][k] + table[i][j][k - k],
                    dp[k][j][k] + table[i][j][k - k],
                )

    for i in range(n +
