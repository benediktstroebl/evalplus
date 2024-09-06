
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """

    if len(lst) < 2:
        return None
    if len(lst) == 2:
        return min(lst)
    m1, m2 = None, None
    for i in range(len(lst)):
        if m1 == None:
            m1 = lst[i]
            continue
        if m1 > lst[i]:
            m2 = m1
            m1 = lst[i]
            continue
        if m2 == None:
            m2 = lst[i]
            continue
        if m2 > lst[i]:
            m2 = lst[i]
    return m2
    
    
