
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Find the max value in arr
    max_val = max(arr)
    # Create a dictionary to map values and their indices in arr
    dict_map = {}
    for i in range(len(arr)):
        dict_map[arr[i]] = i

    # Iterate through the map to get the first element whose value is less than
    # or equal to the current element
    result = []
    for i in range(max_val, 0, -1):
        if i in dict_map:
            result.append(dict_map[i])
        if i - 1 in dict_map:
            result.append(result[-1])

    result.append(-1)

    return result

