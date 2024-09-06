
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
    # temp = [int(d) for d in str(x)]
    # final_list = [item for item in temp if item % 2 != 0]
    # final_list.sort()

    # return final_list

    final_list = []
    temp = [int(d) for d in str(x)]
    for item in temp:
        if item % 2 != 0:
            final_list.append(item)

    final_list.sort()

    return final_list

     
