
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
    # Write your code here.
    arr = []
    for i in x:
        if(i % 10 == 0):
            arr.append(i)
        else:
            arr.append(i)
    #print(arr)
    return sorted(arr)
