
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
    """
    solution:
    if x == []:
        return []
    return sorted(set(x))       
    """
    """  
    solution with duplicates:
    if x == []:
        return []
    new_x = list(set(x))
    new_x.sort()
    return new_x
    """
    """
    solution with sorting:
    if x == []:
        return []
    new_x = x[:]
    new_x.sort()
    return new_x
    """
    """
    solution with itertools:
    import itertools
    if x == []:
        return []
    res = sorted(list(set(x)))
    res2 = []
    for i in res:
        for j in x:
            if i != j and int(str(i)+str(j)) % 2 == 0:
                break
        else:
            res2.append(i)
    return res2
    """
    """
    solution with library:
    import itertools
    if x == []:
        return []
    return [i for i in sorted(set(x)) if i%2==0]
    """
    """
    solution with reduce:
    if x == []:
        return []
    return [reduce(lambda x, y: int(str(x)+str(y)), 
             [i for i in range(1, int(max(x))+1) if i not in x])]
    """
    """
    solution with generator:
    import itertools
    if x == []:
        return []
    return sorted(set([i for i in range(1, int(max(x))+1) 
                    if i not in itertools.chain.from_iterable(x)]))
    """
