

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Variant 1
    max_el = None
    for el in l:
        if max_el is None or el > max_el:
            max_el = el
    return max_el

    # Variant 2
    return max(l)

    # Variant 3
    return l[max(i for i, el in enumerate(l) if el == max(l))]

    # Variant 4
    return l[l.index(max(l))]


