
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

    """
    Method 1: Brute Force (TLE)
    TC: O(n^2)
    SC: O(1)
    """
    # n = len(arr)
    # ans = n
    # for i in range(n):
    #     cnt = 0
    #     for j in range(i + 1, n):
    #         if arr[i] > arr[j]:
    #             cnt += 1
    #     ans = min(ans, cnt)

    """
    Method 2: Dynamic Programming
    TC: O(n^2)
    SC: O(n)
    """
    n = len(arr)
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        dp[i] = n
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                dp[i] = min(dp[i], 1 + dp[j])
    return dp[0]

