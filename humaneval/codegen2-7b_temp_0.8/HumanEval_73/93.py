
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
    arr_length = len(arr)
    if arr_length < 2:
        return 0
    dp = [[1 for _ in range(arr_length + 1)] for _ in range(arr_length + 1)]
    for i in range(2, arr_length + 1):
        for j in range(1, i):
            if arr[j-1] == arr[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
    return dp[arr_length][arr_length
