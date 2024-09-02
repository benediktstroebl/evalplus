

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    "*** YOUR CODE HERE ***"
    if len(l) == 0:
        return True
    l1 = l[0]
    if l1 <= t:
        return below_threshold(l[1:], t)
    else:
        return False

