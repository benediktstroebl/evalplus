
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # {key: value}
    # {key: index}
    # {key: (index, value)}
    largest = {}
    for i, num in enumerate(arr):
        # i - 1 to account for indexing at 0
        # Selection
        if num <= largest.get(num - 1, -1):
            largest[num] = i
    return largest.get(len(arr) - 1, -1)
