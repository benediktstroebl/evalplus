

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    k = len(l)
    for i in l:
        if i >= t:
            k -= 1
    if k == 0:
        return True
    else:
        return False
