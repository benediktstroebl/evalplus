
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
    digits = []
    for num in x:
        digits.append(sum(num % d + d // 2 for d in range(10)))
    digits.sort()
    return [x[i] for i, x in enumerate(digits) if x % 2 == 0]
