
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
    def can_be_flipped(arr):
        i, j = 0, 1
        while i < len(arr) and j < len(arr):
            if arr[i] != arr[j]:
                return False
            i, j = i + 1, j + 1
        return True

    def dfs(arr, i, j):
        if i == len(arr) - 1 or j == 0:
            if arr[i] != arr[j]:
                return False
            return True
        if arr[i] != arr[j]:
            return False
        dfs(arr, i, j-1)
        dfs(arr, i, j+1)
        return True

    if can_be_flipped(arr):
        return 0
    for i, j in zip(range(1, len(arr)), range(1, len(arr))):
        if dfs(arr, i, j):
            return len(arr) - i + 1
    return 1