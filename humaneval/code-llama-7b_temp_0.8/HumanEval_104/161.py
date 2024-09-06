
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
    # if x is None:
    #     return None
    
    # if not x:
    #     return []

    # is_sorted = False
    # while not is_sorted:
    #     is_sorted = True
    #     for i in range(len(x) - 1):
    #         if x[i] > x[i + 1]:
    #             x[i], x[i + 1] = x[i + 1], x[i]
    #             is_sorted = False
    
    # return [i for i in x if not '2' in str(i) and not '4' in str(i) and not '6' in str(i) and not '8' in str(i)]

    if x is None:
        return None
    
    if not x:
        return []

    x.sort()
    
    results = []
    prev_element = x[0]
    results.append(prev_element)

    for i in range(1, len(x)):
        element = x[i]
        if element != prev_element:
            results.append(element)
        prev_element = element

    return [i for i in results if not '2' in str(i) and not '4' in str(i) and not '6' in str(i) and not '8' in str(i)]
