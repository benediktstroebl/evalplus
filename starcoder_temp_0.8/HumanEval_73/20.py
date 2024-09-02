
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
    # Your code here
    n = len(arr)
    print("arr", arr)
    arr = [0] + arr + [0]
    print("arr", arr)
    dp = [[0 for j in range(n+2)] for i in range(n+2)]
    print("dp", dp)
    for i in range(n+1):
        dp[i][i] = 0

    print("dp", dp)
    for gap in range(1, n+1):
        for i in range(n+1):
            j = i + gap
            if j > n:
                break
            dp[i][j] = 1 + min(dp[i+1][j-1], abs(arr[i] - arr[j]))
    print("dp", dp)
    return dp[0][n+1]
