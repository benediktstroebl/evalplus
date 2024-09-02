
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
    if len(lst) == 0 or len(lst) == 1:
        return None
    
    small_element = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] < small_element:
            small_element = lst[i]
    
    second_small_element = small_element
    
    for i in range(0, len(lst)):
        if lst[i] < second_small_element and lst[i] > small_element:
            second_small_element = lst[i]
    
    return second_small_element
