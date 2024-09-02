

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # assume all are below threshold to start with
    all_below = True

    # check each number in list
    for number in l:
        if number > t:
            all_below = False

    return all_below
