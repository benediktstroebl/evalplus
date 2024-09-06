
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
    
    def dfs(arr, index):
        if len(arr) == index:
            return 0

        min_val = float("inf")
        for i in range(index, len(arr)):
            if arr[index] == arr[i] and i - index < min_val:
                min_val = i - index
        
        if min_val!= float("inf"):
            dfs(arr, index+1)
        dfs(arr, index+1)
    
    dfs(arr, 0)
    return min(dfs(arr, 0), len(arr) - dfs(arr, 0
