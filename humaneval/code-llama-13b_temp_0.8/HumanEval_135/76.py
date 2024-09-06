
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
    max_value = max(arr)
    if max_value ** 2 > sum(arr):
        return -1
    if sum(arr) % 2:
        return -1
    total = 0
    for n in arr:
        total += n
    total /= 2
    if total not in arr:
        return -1
    return arr.index(total)

