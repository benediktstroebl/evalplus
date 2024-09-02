
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    for index in range(len(arr)):
        if index == 0 or arr[index - 1] < arr[index]:
            maximum = index
            break
    else:
        return -1
    for index in range(len(arr) - 1, -1, -1):
        if index == len(arr) - 1 or arr[index] > arr[index - 1]:
            minimum = index
            break
    return (len(arr) - 1) - (maximum - minimum)

