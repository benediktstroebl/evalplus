

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    count = 0
    for num in l:
        if num < t:
            count += 1
    if count == len(l):
        return True
    else:
        return False

