

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # use default sorting if available
    if sys.version_info >= (3, 7):
        return sorted(l, key=lambda x: x if x != x else None)
    else:
        return sorted(l)