
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
    
    if len(lst) == 0:
        return None
    
    min_element = max_element = lst[0]
    lst_iter = iter(lst)
    next(lst_iter)
    
    for i in lst_iter:
        if i < min_element:
            min_element = i
        elif min_element < i < max_element:
            max_element = i
    
    if max_element != min_element:
        return max_element
    return None
    
