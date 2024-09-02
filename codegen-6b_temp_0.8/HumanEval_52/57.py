

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # new_l = [t if i > t else i for i in l]
    # return new_l == l
    return all(i <= t for i in l) 
