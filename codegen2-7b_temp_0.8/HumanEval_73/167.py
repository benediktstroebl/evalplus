
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

    def isPalindrom(arr):
        if arr[0]!= arr[-1]:
            return False
        return arr[0] == arr[0]

    dp = [[[False for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i][0] = True
    for i in range(1, n):
        for j in range(i):
            for k in range(j, i):
                dp[i][j][k] = dp[i - 1][j][k] or isPalindrom(arr[j:k + 1])

    
