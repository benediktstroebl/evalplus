

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    # Go through each element in the list, and if any of them are above the threshold return False.
    for element in l:
        if element >= t:
            return False

    # If no elements are above the threshold, return True
    return True

