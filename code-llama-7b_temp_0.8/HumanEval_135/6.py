
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # For each element, check if the element is greater than or equal to the
    # previous element. If it is, check if the previous element can be placed
    # at the location of the element.
    #
    # If the current element is greater than the previous element, then the
    # previous element must be in the location of the current element. If the
    # current element is less than or equal to the previous element, then the
    # previous element cannot be placed at the location of the current element.
    #
    # Check if the previous element can be placed at the location of the
    # current element. If it cannot, then set the previous element equal to the
    # current element and set the current element equal to the previous
    # element.

    # Time: O(n)
    # Space: O(1)
    prev = 0
    i = 1
    while i < len(arr):
        if arr[i] >= arr[i - 1]:
            prev = arr[i - 1]
            arr[i - 1] = arr[i]
            arr[i] = prev
            i -= 1
            continue
        elif arr[i] < prev:
            return -1

        i += 1

    return i - 1

