
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

    # 1.5 points
    even_digits = []
    for i in x:
        for j in range(0, len(str(i))):
            if j%2 == 0:
                even_digits.append(int(str(i)[j]))
    even_digits.sort()
    even_digits = list(set(even_digits))
    even_digits.sort()
    return x[~(x % even_digits)]
