
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

    def is_palindromic(arr, l, r):
        while l < r:
            if arr[l]!= arr[r]:
                return False
            l += 1
            r -= 1
        return True

    arr.sort()
    print(arr)
    n = len(arr)
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if is_palindromic(arr, i, j):
                dp[i] = 0
                break
            else:
                dp[i] = min(dp[i], dp[j] + 1)
    print(dp)
    return dp[0]

