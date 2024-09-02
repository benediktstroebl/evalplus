

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    def sign(x):
        if x == 0:
            return 0
        elif x > 0:
            return 1
        else:
            return -1

    return [x for x in l if sign(x) >= 0]
