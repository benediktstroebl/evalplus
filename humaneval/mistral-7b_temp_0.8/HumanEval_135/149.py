
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    start_idx = 0
    end_idx = len(arr) - 1

    while start_idx <= end_idx:
        # We move the start index until it is equal to the end index and
        # we find a value that is less than the previous one.
        while start_idx <= end_idx and arr[start_idx] <= arr[start_idx - 1]:
            start_idx += 1
        # Once we have found the position, we can break the loop.
        break

    # If the start index and the end index are equal, then there is no
    # element with a value that is less than the previous one.
    if start_idx == end_idx:
        return -1

    return start_idx - 1

