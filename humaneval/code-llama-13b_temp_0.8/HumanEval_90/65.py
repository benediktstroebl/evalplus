
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
    
    min_element = None
    next_min_element = None
    for elem in lst:
        if min_element == None or elem < min_element:
            next_min_element = min_element
            min_element = elem
        elif next_min_element == None or elem < next_min_element:
            next_min_element = elem
    return next_min_element

