

def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # This will work for a list of numbers.
    # But, it will not work for a list of strings.
    # I think you have to know the type of the list.
    # How do we do this?
    # return [x + 1 for x in l]

    # Using type hinting, we can enforce the type of the list,
    # so the function can be used for a list of any type.
    return [x + 1 for x in l]

