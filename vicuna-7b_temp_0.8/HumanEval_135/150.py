
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    low_index = 0
    high_index = len(arr) - 1
    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2
        if arr[mid_index] < arr[mid_index - 1]:
            low_index = mid_index + 1
        elif arr[mid_index] > arr[mid_index + 1]:
            high_index = mid_index - 1
        else:
            return mid_index
