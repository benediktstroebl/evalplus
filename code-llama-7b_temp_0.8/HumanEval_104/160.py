
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
    lst = []
    for i in x:
        if i < 0:
            raise ValueError("input is negative")
        else:
            lst.append(i)
    a = []
    for i in range(len(lst)):
        s = str(lst[i])
        for j in range(len(s)):
            if int(s[j]) % 2 == 0:
                lst[i] = lst[i] - int(s[j])
                s = str(lst[i])
    for i in range(len(lst)):
        s = str(lst[i])
        for j in range(len(s)):
            if int(s[j]) % 2 == 0:
                break
        else:
            a.append(lst[i])
    a.sort()
    return a
