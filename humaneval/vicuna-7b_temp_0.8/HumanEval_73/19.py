
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
    def dfs(arr, i, j):
        if i == len(arr)-1 or j == 0 or j == len(arr) - 1:
            return
        arr[i][j] = arr[i][j] + arr[i][dfs(arr, i+1, j-1)][0]
        dfs(arr, i+1, j-1)
        arr[i][j] = arr[i][j] - arr[i][dfs(arr, i+1, j-1)][0]
        dfs(arr, i+1, j-1)

    for i in range(len(arr)):
        for j in range(1, len(arr)):
            dfs(arr, i, j)
    return len(arr)
