
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    return sorted([i for i in x if not 0 in str(i) and not 2 in str(i) and not 4 in str(i) and not 6 in str(i) and not 8 in str(i) and not 10 in str(i) and not 12 in str(i) and not 14 in str(i) and not 16 in str(i) and not 18 in str(i) and not 20 in str(i) and not 22 in str(i) and not 24 in str(i) and not 26 in str(i) and not 28 in str(i) and not 30 in str(i) and not 32 in str(i) and not 34 in str(i) and not 36 in str(i) and not 38 in str(i) and not 40 in str(i) and not 42 in str(i) and not 44 in str(i) and not 46 in str(i) and not 48 in str(i) and not 50 in str(i) and not 52 in str(i) and not 54 in str(i) and not 56 in str(i) and not 58 in str(i) and not 60 in str(i) and not 62 in str(i) and not 64 in str(i) and not 66 in str(i) and not 68 in str(i) and not 70 in str(i) and not 72 in str(i) and not 74 in str(i) and not 76 in str(i) and not 78 in str(i) and not 80 in str(i) and not 82 in str(i) and not 84 in str(i) and not 86 in str(i) and not 88 in str(i) and not 90 in str(i) and not 92 in str(i) and not 94 in str(i) and not 96 in str(i) and not 98 in str(i)])


