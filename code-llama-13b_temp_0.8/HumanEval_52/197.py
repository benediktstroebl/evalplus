

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # hint1: for loop to check all elements one by one
    # hint2: use boolean, logical operator, and
    res = True
    for e in l:
        if e > t:
            res = False
    return res

