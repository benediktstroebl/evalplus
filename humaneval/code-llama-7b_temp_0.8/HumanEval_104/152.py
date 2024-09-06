
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
    out = []
    for num in x:
        num = str(num)
        if num.find('2') == -1 and num.find('4') == -1 and num.find('6') == -1 and num.find('8') == -1:
            out.append(int(num))
    return sorted(out)

