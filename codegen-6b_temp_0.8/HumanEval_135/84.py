
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) < 2:
        return -1

    pairs = defaultdict(int)
    for i in range(1, len(arr)):
        if arr[i - 1] < arr[i]:
            pairs[arr[i - 1]] += 1

    max_index = 0
    for i in range(1, len(arr)):
        if pairs[arr[i]] > 0:
            pairs[arr[i]] -= 1
            max_index = max(max_index, i)

    return max_index
