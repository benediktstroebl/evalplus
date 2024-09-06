

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # check for empty list
    if l == []:
        raise ValueError('empty list: can not find max element')
    # get max element
    max_el = l[0]
    for elem in l:
        if elem > max_el:
            max_el = elem
    return max_el
