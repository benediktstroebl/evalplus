
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
    
    m1 = lst[0]
    m2 = None
    
    for i in range(1, len(lst)):
        if lst[i] < m1:
            m1 = lst[i]
        elif m2 == None and m1 < lst[i]:
            m2 = lst[i]
    
    return m2
