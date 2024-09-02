
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
    
    s_lst = []
    for n in lst:
        if n not in s_lst:
            s_lst.append(n)
    
    s_lst = sorted(s_lst)
    if len(s_lst) < 2:
        return None
    
    return s_lst[1]
