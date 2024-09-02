

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    assert len(l) > 0, "You need a list with at least one item."
    assert t >= 0, "The threshold must be a positive number."
    return all(x <= t for x in l)
