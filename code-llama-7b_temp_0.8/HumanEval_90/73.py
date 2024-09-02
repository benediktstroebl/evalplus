
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

    lst = sorted(lst)
    if len(lst) == 1 or len(lst) == 2:
        return None
    return lst[1]
    
    #return lst[lst.index(min(lst))+1]
    
    #return sorted(lst)[1]
    
    #lst.sort()
    #return lst[1]
    
    #return sorted(lst)[len(lst)-2]
    
    #min_val = min(lst)
    #return sorted([x for x in lst if x > min_val])[0]
    
    #if len(lst) == 2:
    #    return None
    #for x in lst:
    #    if x > min(lst):
    #        return x
    #return None
