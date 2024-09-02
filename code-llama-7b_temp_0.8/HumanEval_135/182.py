
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Calculate the result
    # The starting value is the smallest value in the array
    arr.sort()
    #print("arr: {}".format(arr))

    result = -1
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] >= smallest:
            smallest = arr[i]
            result = i

    return result
