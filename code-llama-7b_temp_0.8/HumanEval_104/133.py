
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
    # result = []
    # for i in x:
    #     if '2' not in str(i):
    #         if '3' not in str(i):
    #             if '4' not in str(i):
    #                 if '5' not in str(i):
    #                     if '6' not in str(i):
    #                         if '7' not in str(i):
    #                             if '8' not in str(i):
    #                                 if '9' not in str(i):
    #                                     result.append(i)
    # return sorted(result)

    result = []
    for i in x:
        for j in str(i):
            if int(j) % 2 == 0:
                break
        else:
            result.append(i)
    return sorted(result)

