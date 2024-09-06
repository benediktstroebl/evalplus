

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # return function
    # return all([True if x<t else False for x in l])
    # return all([x<t for x in l])
    return not any([x>t for x in l])
