
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # TODO: Write your can_arrange function here.
    # can_arrange([1,2,4,3,5]) = 3
    # The largest index is 4 because 4 <= 3

    # can_arrange([1,2,3]) = -1
    # There is no larger index than 2, so we return -1
    largest_index = -1

    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            largest_index = i - 1

    return largest_index

