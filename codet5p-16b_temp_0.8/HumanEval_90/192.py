
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

    
    smallest = None
    for value in lst:
        if smallest == None:
            smallest = value
        if value < smallest:
            smallest = value
        if value > smallest:
            break
    
    lst.remove(smallest)
    
    if len(lst) > 0:
        return lst[0]
    
    return None
