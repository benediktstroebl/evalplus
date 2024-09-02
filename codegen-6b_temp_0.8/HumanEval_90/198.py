
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
    
    ret = None
    
    try:
        sorted_list = sorted(lst)
        if len(sorted_list) == 0:
            return None
        elif len(sorted_list) == 1:
            return sorted_list[0]
        elif len(sorted_list) == 2:
            return sorted_list[1]
        elif len(lst) > 2:
            ret = sorted_list[1]
    except:
        ret = None
    
    return ret
