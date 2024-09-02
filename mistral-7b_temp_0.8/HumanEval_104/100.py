
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
    
    # Yo yo yo
    
    res = []
    for i in x:
        a = list(str(i))
        if all(int(j)%2!=0 for j in a):
            res.append(i)
    return sorted(res)
    
    # This solution is very ugly, but we need to practice the list comprehension 
    # somehow. 
    # ls = []
    # for num in x:
    #     if all(int(n) % 2 != 0 for n in str(num)):
    #         ls.append(num)
    # return sorted(ls)
    
    # return sorted(x for x in x if all(int(n) % 2 != 0 for n in str(x)))
    
    # return sorted([x for x in x if all(int(n) % 2 != 0 for n in str(x))])
    
    # return sorted([x for x in x if all(int(n) % 2 != 0 for n in str(x))])
    
    #
