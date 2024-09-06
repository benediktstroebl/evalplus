
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
    digit = 0
    while x:
        while x[0] % 2 == 0:
            x = x[1:]
        yield x[0]
        x = x[1:]
        while x:
            while x[0] % 2 == 0:
                x = x[1:]
            yield x[0]
            x = x[1:]

x = [15, 33, 1422, 1]
for d in unique_digits(x):
    print(d)
