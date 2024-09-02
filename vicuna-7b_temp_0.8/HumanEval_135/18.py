
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # check if the arr is empty
    if not arr:
        return -1
    
    # sort the arr
    arr = sorted(arr)
    
    # check if the last element is greater than or equal to the second last
    if arr[-1] >= arr[-2]:
        return -1
    
    # check if the first element is less than the second element
    if arr[0] < arr[1]:
        return 1
    
    # check if the last element is greater than or equal to the first element
    if arr[-1] >= arr[0]:
        return 1
    
    # check if the last element is less than the second to last element
    if arr[-1] < arr[-2]:
        return 1
    
    # check if the last element is greater than or equal to the second to last element
    if arr[-1] >= arr[-2]:
        return 1
    
    # check if the first element is greater than the second to last element
    if arr[0] > arr[-2]:
        return 1
    
    # check if the last element is greater than or equal to the second element
    if arr[-1] >= arr[1]:
        return 1
    
    # check if the last element is less than the first element
    if arr[-1] < arr[0]:
        return 1
    
    # check if the last element is greater than or equal to the first element
    if arr[-1] >= arr[0]:
        return 1
    
    # check if the last element is less than the second element
    if arr[-1] < arr[1]:
        return 1
    
    # check if the last element is greater than or equal to the second element
    if arr[-1] >= arr[1]:
        return 1
    
    # check if the first element is greater than the second element
    if arr[0] > arr[1]:
        return 1
    
    # check if the last element is greater than or equal to the second element
    if arr[-1] >= arr[1]:
        return 1
    
    # check if the last element is less than the first element
    if arr[-
