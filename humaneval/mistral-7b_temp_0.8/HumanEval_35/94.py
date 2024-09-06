

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    def _max_element(l: list, i: int = 0) -> int:
        if len(l) == 1:
            return l[0]
        if l[i] > l[i + 1]:
            return l[i]
        return _max_element(l, i + 1)

    return _max_element(l)
