
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # for element in arr:
    #     if element > arr[arr.index(element)-1]:
    #         return arr.index(element)
    # return -1
    a = [1,2,4,3,5]
    for i in range(1,len(a)):
        if a[i] > a[i-1]:
            return i
    return -1
