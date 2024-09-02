
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
    if len(arr) == 1 or len(arr) == 0:
        return 0
    dp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] == arr[i]:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1])
    print(dp)
    return dp[len(arr) - 1][0]
