
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
    list_cpy = lst.copy()
    list_cpy.sort()
    if len(list_cpy) == 0:
        return None
    if len(list_cpy) < 2:
        return None
    
    for i in range(len(list_cpy) - 1):
        if list_cpy[i] == list_cpy[i+1]:
            continue
        else:
            return list_cpy[i+1]
    return None
