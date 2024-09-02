

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # base case
    if len(l) == 1:
        return l[0]
    # recursive case
    max_elem = max_element(l[:len(l) // 2])
    if max_elem > l[len(l) // 2]:
        return max_elem
    else:
        return max_element(l[len(l) // 2 + 1:])
