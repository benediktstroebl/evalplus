
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # Since the array is sorted and won't contain duplicate values,
    # we can use a linear search to locate the first occurrence
    # of a value which is not greater than the preceding element.
    # If such an element doesn't exist, the function should return -1.

    for i in range(len(arr)):
        if i == 0:
            if arr[i] > arr[i+1]:
                return -1
            else:
                continue
        elif arr[i] > arr[i-1]:
            return -1
        else:
            return i

