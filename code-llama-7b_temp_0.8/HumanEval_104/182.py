
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
    # my initial solution
    # y = []
    # for i in x:
    #     y.append(i)
    #     while any(d % 2 == 0 for d in map(int, str(i))):
    #         y.remove(i)
    #         i = i // 10
    # return y
    # from the internet
    return [i for i in x if not any(d % 2 == 0 for d in map(int, str(i)))]


