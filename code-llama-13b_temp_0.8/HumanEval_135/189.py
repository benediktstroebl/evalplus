
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    n = len(arr)
    if n == 0:
        return 0

    m = max(arr)
    max_element = max(arr)
    freq = [0] * (max_element + 1)
    for element in arr:
        freq[element] += 1
    
    # If there are odd number of elements then we can't rearrange
    odd = 0
    for element in arr:
        odd += freq[element] % 2
    if odd > 0:
        return -1

    idx = n - 1
    for element in range(max_element, -1, -1):
        if freq[element] > 0:
            idx -= freq[element]
            if idx < 0:
                return element
    
    return -1
