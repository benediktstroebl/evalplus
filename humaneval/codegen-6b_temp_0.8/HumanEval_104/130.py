
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
    # results = []
    # for i in x:
    #     digits = [int(digit) for digit in str(i)]
    #     results.append(i) if len(set(digits)) == len(digits) else None
    # return results
    return sorted([i for i in x if len(set(str(i))) == len(str(i))])

