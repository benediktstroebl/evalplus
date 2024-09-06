
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
    # Method 1
    # if not x:
    #     return []
    # else:
    #     return sorted(list(set(map(int,filter(lambda x:x[0]%2==1,map(str,x))))))
    # Same idea but shuffle
    # return sorted([x[i] for i in range(len(x)) if x[i]%2==1])

    # Method 2
    return sorted(set(map(int,filter(lambda x:x[0]%2==1,map(str,x)))))



