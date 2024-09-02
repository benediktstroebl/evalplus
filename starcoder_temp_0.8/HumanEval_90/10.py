
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
    # short_lst = sorted(lst)
    # if short_lst[1] == short_lst[0]:
    #     return None
    # else:
    #     return short_lst[1]
    
    #shorter but more complicated
    
    lst = sorted(lst)
    
    if lst[0] == lst[1]:
        return None
    else:
        return lst[1]
