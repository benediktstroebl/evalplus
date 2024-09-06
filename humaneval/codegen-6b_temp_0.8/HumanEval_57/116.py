

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    def compare(a, b):
        if a == b:
            return 0
        elif a > b:
            return 1
        else:
            return -1
    # for i in range(len(l) - 1):
    #     if compare(l[i], l[i+1]) == 1:
    #         return False
    # return True
    return all(compare(l[i], l[i+1]) == 0 for i in range(len(l) - 1))

