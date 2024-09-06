
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
    
    if len(lst) <= 1:
        return None
    
    n = 2
    
    while n < len(lst):
        if lst[n-1] > lst[n]:
            return lst[n]
        n += 1
    
    return lst[n-
