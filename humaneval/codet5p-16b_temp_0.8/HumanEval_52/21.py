

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    assert l, "List is empty."

    if len(l) == 1 and l[0] > t:
        return False

    return all([x < t for x in l])
