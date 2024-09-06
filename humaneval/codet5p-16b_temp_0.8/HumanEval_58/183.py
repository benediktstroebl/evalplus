

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    def uniq(l: list):
        """Return sorted unique elements for one list.
        >>> uniq([1, 4, 3, 34, 653, 2, 5])
        [1, 2, 3, 4, 5, 653]
        >>> uniq([5, 3, 2, 8])
        [5, 2, 8]

        """
        s = set(l)
        return sorted(s)

    l1_set = uniq(l1)
    l2_set = uniq(l2)
    return sorted(l1_set.intersection(l2_set))

