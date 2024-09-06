

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # If l is empty
    if l == []:
        return True
    # If the first element of l is below threshold t
    if l[0] < t:
        return True
    # If all the other elements in l are below threshold t
    if below_threshold(l[1:], t):
        return True
    # If l is not empty and no elements in l are below threshold t
    return False

