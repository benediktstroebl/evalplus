

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # get length of list
    length = len(l)

    # compare list[0] and list[1]
    comparison = l[0] - l[1]

    # set initial state of monotonic
    monotonic = True

    # if list[0] and list[1] are equal set state to True
    if comparison == 0:
        monotonic = True

    # if list[0] is less than list[1] set state to True
    if comparison < 0:
        monotonic = True

    # if list[0] is greater than list[1] set state to False
    if comparison > 0:
        monotonic = False

    # loop through list if list is length 2 or greater
    if length > 2:
        for index in range(1, length - 1):
            # get difference of current index and next index
            comparison = l[index] - l[index + 1]
            # if difference is negative set state to False
            if comparison < 0:
                monotonic = False
            # if difference is positive set state to True
            if comparison > 0:
                monotonic = True

    return monotonic
