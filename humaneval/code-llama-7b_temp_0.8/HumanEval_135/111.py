
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if not arr:
        return -1
    elif len(arr) == 1:
        return 0

    # Initialize a dictionary to keep track of maximum value in array
    # and corresponding index
    max_dict = {0: 0, arr[0]: 0}

    for i in range(1, len(arr)):
        # Update index of maximum value
        max_dict[arr[i - 1]] = max(max_dict[arr[i - 1]], i - 1)

        # Update index of maximum value in array
        max_dict[arr[i]] = max(max_dict[arr[i]], i)

    # Initialize index of maximum value
    max_index = 0

    # Iterate through dictionary and update index of maximum value
    for key in max_dict:
        if max_dict[key] > max_index:
            max_index = max_dict[key]

    # Check if last element in array is greater than or equal to max value
    if arr[max_index] >= arr[-1]:
        return -1

    return max_index


