
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
    # Your code here
    list1 = []
    list2 = []
    for i in x:
        str_i = str(i)
        for j in str_i:
            if int(j)%2 == 0:
                list1.append(i)
            else:
                list2.append(i)
    return sorted(list2)

    # Another way
    # return sorted(set(x) - set(n for n in x if any(d in '02468' for d in str(n))))

    # One more
    # return sorted(set(i for i in x if not any(d in '02468' for d in str(i))))

    

