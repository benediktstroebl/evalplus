
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
    def dfs(arr, change, l, r):
        if r >= l:
            return
        for i in range(l, r+1):
            if arr[i] != arr[i-change]:
                return
            arr[i], arr[i-change] = arr[i-change], arr[i]
            change -= 1
            dfs(arr, change, l, i-1)
            dfs(arr, change, i+1, r)
            change += 1
    
    return dfs(arr, 0, 0, len(arr)-1)
