
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
    output = []
    for n in x:
        if n > 0:
            # 1. extract digits
            digits = str(n)
            # 2. check if there is an even digit
            evens = [int(d) for d in digits if int(d) % 2 == 0]
            if len(evens) == 0:
                output.append(n)
    return sorted(output)
