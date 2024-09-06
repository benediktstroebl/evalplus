
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
    hmap = {}
    result = []
    for num in x:
        s = str(num)
        for ch in s:
            hmap[ch] = hmap.get(ch, 0) + 1
    for k, v in hmap.iteritems():
        if v % 2 == 1:
            continue
        else:
            result.append(k*(v/2))
    return sorted(result)
