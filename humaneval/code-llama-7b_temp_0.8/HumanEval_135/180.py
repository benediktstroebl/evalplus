
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr_max = max(arr)
    if arr_max == 0:
        return -1
    arr_min = min(arr)

    #create new array to hold index of each element in original array
    new_arr = [0] * (arr_max + 1)
    for i in range(0, len(arr)):
        new_arr[arr[i]] = i

    #iterate through the new array
    #check if new_arr[i] is greater than or equal to new_arr[i-1]
    #if so, return the index of the element that is not >= i-1
    #otherwise, keep iterating until new_arr[i] is less than new_arr[i-1]
    i = 1
    while i < len(new_arr) and new_arr[i] >= new_arr[i-1]:
        i += 1
    if new_arr[i] < new_arr[i-1]:
        return new_arr[i]
    return -1

