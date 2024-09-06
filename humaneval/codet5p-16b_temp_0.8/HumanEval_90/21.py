
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
    
    smallest = min(lst)
    ind_smallest = lst.index(smallest)
    
    if ind_smallest == 0:
        return None
    
    if lst[ind_smallest - 1] > smallest:
        return lst[ind_smallest - 1]
    
    if ind_smallest == len(lst) - 1:
        return None
    
    return lst[ind_smallest + 1]
