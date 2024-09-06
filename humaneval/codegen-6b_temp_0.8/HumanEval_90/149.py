
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
    if len(lst) < 1:
        return None
    nsmallest = lst[0]
    nsmallest_pos = 0
    for i, v in enumerate(lst):
        if v <= nsmallest:
            nsmallest = v
            nsmallest_pos = i
    if nsmallest_pos + 1 < len(lst):
        return lst[nsmallest_pos + 1]
    else:
        return None

