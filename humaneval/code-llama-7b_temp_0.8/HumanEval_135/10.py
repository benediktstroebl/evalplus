
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) <= 1:
        return -1

    # for each element, save the largest index of an element which is not greater than or equal to it
    # this will give O(n) runtime
    max_indices = [-1] * len(arr)

    # since this is a nondecreasing array, the largest element is the last one
    # this will give us O(n) runtime
    largest_element = arr[-1]
    max_indices[-1] = len(arr) - 1

    # this will give us O(n) runtime
    for i in range(len(arr) - 2, -1, -1):
        # since this is a nondecreasing array, any element which is greater than the current one
        # is not greater than or equal to it
        if arr[i] <= largest_element:
            max_indices[i] = len(arr) - 1
            largest_element = max(largest_element, arr[i])
        else:
            max_indices[i] = max_indices[i + 1] - 1

    return max_indices[0]
