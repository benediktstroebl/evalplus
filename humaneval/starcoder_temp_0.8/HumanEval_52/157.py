

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    "*** YOUR CODE HERE ***"
    result = True
    for n in l:
        if n > t:
            result = False
            break
    return result
