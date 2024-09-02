

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    # Recommended Solution:
    # return sorted(set(l))

    # Ordered Dictionary is a map
    from collections import OrderedDict
    return list(OrderedDict.fromkeys(l).keys())

    # Sets are unordered
    return sorted(set(l))

