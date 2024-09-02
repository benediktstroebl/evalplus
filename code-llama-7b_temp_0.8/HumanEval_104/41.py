
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
    for element in x:
        #convert element to string
        element = str(element)
        #store only those element which has no even digits
        if not '2' in element and not '4' in element and not '6' in element and not '8' in element:
            output.append(element)
    #sort the output in ascending order
    output.sort()
    return output


