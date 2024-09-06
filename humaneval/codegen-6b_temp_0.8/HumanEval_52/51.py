

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    res, n = True, 0

    for i in l:
        if i >= t:
            n += 1
    if n == 0 or n == len(l) - 1:
        res = False
    return res
