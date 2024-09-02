
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
    x = list(x)
    for num in x:
        for i in range(1, len(str(num))):
            if sum(int(digit) for digit in str(num)) % 2 == 0:
                x.remove(num)
                break
    return x
