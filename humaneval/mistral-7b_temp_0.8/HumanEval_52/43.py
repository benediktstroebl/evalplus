

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    # if all numbers in the list are below threshold t, then it returns True
    # else it returns False

    for number in l:
        if number < t:
            continue
        else:
            return False

    return True

