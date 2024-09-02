
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
    #     str_i = str(i)
    #     if str_i.count("2") == 0 and str_i.count("4") == 0 and str_i.count("6") == 0 and str_i.count("8") == 0:
    #         result.append(i)
    # return sorted(result)

    # return [i for i in x if not set(str(i)).intersection({"2", "4", "6", "8"})]

    # unique_digits = lambda x: sorted(i for i in x if not set(str(i)).intersection({"2", "4", "6", "8"}))

    return sorted(i for i in x if not "2" in str(i) and not "4" in str(i) and not "6" in str(i) and not "8" in str(i))
