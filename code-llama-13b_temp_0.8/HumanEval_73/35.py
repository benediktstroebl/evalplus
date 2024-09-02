
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
    if n == 0 or n == 1:
        return 0
    f = [[0] * n for _ in range(n)]
    for i in range(n):
        f[i][i] = 0
    # f[i][j] is the min number of changes for the i-j subarray
    for l in range(2, n+1):
        for i in range(n - l + 1):
            j = i + l - 1
            f[i][j] = float('inf')
            # consider not changing the array at all
            if i == j:
                f[i][j] = 0
            # consider changing the first element
            if i + 1 < j:
                f[i][j] = min(f[i][j], f[i+1][j] + 1)
            # consider changing the last element
            if i + 1 < j:
                f[i][j] = min(f[i][j], f[i][j-1] + 1)
            # consider changing the middle two elements
            if i + 2 <= j - 2:
                f[i][j] = min(f[i][j], f[i+2][j-2] + 1)
    return f[0][n-1]

