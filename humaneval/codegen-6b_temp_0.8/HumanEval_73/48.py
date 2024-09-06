
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
    # dp[i] is the minimum number of steps to make arr[i:] or arr[:i] palindromic
    dp = [0] * len(arr)
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            dp[i] = dp[i - 1]
        else:
            for j in range(i):
                if arr[j] == arr[i] - 1:
                    # dp[i] = min(dp[i], dp[j] + 1)
                    # elif arr[i] == arr[j] + 1:
                    #     dp[i] = min(dp[i], dp[j])
                    dp[i] = min(dp[i], 1 + dp[j])
    return dp[-1]

