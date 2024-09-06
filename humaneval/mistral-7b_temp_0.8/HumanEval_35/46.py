

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    def check_max(l, i):
        if not l:
            return None
        if i == 0:
            return l[i]
        else:
            return max(l[i], check_max(l, i - 1))

    return check_max(l, len(l) - 1)

