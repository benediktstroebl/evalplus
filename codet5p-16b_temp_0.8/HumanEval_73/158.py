
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

    
    if len(arr) == 1:
        return 0
    
    if len(arr) == 2:
        if arr[0] == arr[1]:
            return 0
        if arr[0]!= arr[1]:
            return 1
    
    arr_unique = set(arr)
    min_changes = len(arr) - len(arr_unique)
    
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                new_arr = arr[0:i] + [arr[j]] + arr[i+1:j] + [arr[i]] + arr[j+1:]
                min_changes = min(min_changes, smallest_change(new_arr))
    
    return min_changes



