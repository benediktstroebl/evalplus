

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    if len(l) == 1:
        return l

    # First, sort the list
    l = sorted(l)

    # Next, check the first element, if it is equal to the second one
    # we know that all the rest will be equal to the first
    # so we return the first element
    if l[0] == l[1]:
        return [l[0]]

    # Next, we check if the second element is equal to the third
    # if it is equal to the third we know that all the rest will be equal
    # so we return the second element
    if l[1] == l[2]:
        return [l[1]]

    # Finally we check if the third element is equal to the fourth
    # if it is equal to the fourth we know that all the rest will be equal
    # so we return the third element
    if l[2] == l[3]:
        return [l[2]]

    # We've checked the first three elements
    # so all the elements after them are unique
    return [l[0]] +
