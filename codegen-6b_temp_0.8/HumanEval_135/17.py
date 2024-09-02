
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    index_cache = {}
    for i in range(len(arr)):
        if i not in index_cache:
            previous_num = arr[i-1] if i > 0 else -1
            previous_index = i-1
            if previous_num >= arr[i]:
                index_cache[previous_num] = previous_index
        else:
            previous_index = index_cache[previous_num]
            if previous_index >= i-1:
                return previous_index
            index_cache[arr[i]] = i
    return -1

