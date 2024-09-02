

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # if l is empty, return an error
    if len(l) == 0:
        return "The list is empty, please enter a list."
    # otherwise, the maximum element is the first element in the list
    max_elem = l[0]
    # scan the list for the maximum element
    for elem in l:
        if elem > max_elem:
            max_elem = elem
    return max_elem

