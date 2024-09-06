
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) == 1:
        return -1

    if len(arr) == 2:
        return 1 if arr[0] >= arr[1] else 0

    # precompute all sums
    sums = []
    current = 0
    for i in arr:
        current += i
        sums.append(current)
    for i in range(len(sums) - 1):
        sums[i] = sums[i] % 6

    # loop through sums to find a value which
    # is smaller than a value immediately preceding it
    last_idx = len(sums) - 1
    for i, sum in enumerate(sums[:-1]):
        if i == last_idx:
            return -1
        if sums[i] > sums[i + 1]:
            return i

    return -1

