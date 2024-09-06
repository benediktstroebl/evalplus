

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    """
    my_list = list(l)
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            return False
    return True
    """
    return (l[0] <= l[-1]) and all(l[i] <= l[i + 1] for i in range(len(l) - 1))

