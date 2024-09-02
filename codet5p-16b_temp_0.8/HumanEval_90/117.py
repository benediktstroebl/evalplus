
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

    if lst == []:
        return None
    if len(lst) == 1:
        return None
    
    min_elem = lst[0]
    min_index = 0
    for i in range(len(lst)):
        if lst[i] < min_elem:
            min_elem = lst[i]
            min_index = i
    
    if min_index == 0:
        if len(lst) == 2:
            return None
        if len(lst) == 3:
            return None
        min_index = 2
    
    return lst[min_index]
