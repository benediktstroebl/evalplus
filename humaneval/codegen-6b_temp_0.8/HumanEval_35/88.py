

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Handle empty list.
    if not l:
        return None

    # Handle lists of size 1.
    if len(l) == 1:
        return l[0]

    # Handle lists with only a single element.
    if len(l) == 2:
        return max(l[0], l[1])

    # If there are several elements that are the maximum,
    # return the element with the largest index
    # that is greater than 1.
    max_ind = 1
    for i in range(1, len(l)):
        if l[i] > l[max_ind]:
            max_ind = i

    return l[max_ind]
