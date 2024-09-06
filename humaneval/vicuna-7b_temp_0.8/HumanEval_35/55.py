

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # if the list is empty, return -1
    if not l:
        return -1

    # if the list is just one element, return that element
    if len(l) == 1:
        return l[0]

    # if the list is sorted, return the first element
    if sorted(l):
        return l[0]

    # sort the list in non-descending order
    l.sort(reverse=True)

    # return the first element
    return l[0]
