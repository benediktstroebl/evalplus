
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
    def dfs(arr, mark, i, j):
        if i == len(arr) or j == 0 or j == len(arr[0]):
            return
        if arr[i] == arr[j]:
            mark *= 2
            dfs(arr, mark, i+1, j-1)
            dfs(arr, mark, i-1, j-1)
        else:
            mark *= 2
            dfs(arr, mark, i+1, j)
            dfs(arr, mark, i-1, j)
            dfs(arr, mark, i, j+1)
            dfs(arr, mark, i, j-1)
            
    mark = 1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            dfs(arr, mark, i, j)
        mark = 1 / mark
    return mark