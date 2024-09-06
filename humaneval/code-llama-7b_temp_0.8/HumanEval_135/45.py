
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Find the largest element that is not greater than the largest element preceding it.
    # Start with the largest element and move to the left. If the preceding element is
    # larger than the current element, then the largest element not greater than the
    # preceding element is the current element.
    # For example, given [1,2,3,4,5], the largest element which is not greater than the
    # preceding element is 3, so that's the answer.

    if len(arr) == 0:
        return -1

    result = -1
    largest = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] <= largest:
            result = i
            largest = arr[i]

    return result

