
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Check that all elements are positive
    for elem in arr:
        if elem < 0:
            return -1
    # Check that the largest element is less than sum of all elements
    if max(arr) > sum(arr):
        return -1
    # Get the set of integers from 1 to the maximum array element
    # Remove elements that are in arr
    # Check if the remaining elements are empty
    # If they are not return -1, otherwise return the max value
    possible = set(range(1, max(arr) + 1))
    for num in arr:
        if num in possible:
            possible.remove(num)
    if not possible:
        return -1
    return max(possible)

