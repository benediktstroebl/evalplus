
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
    
    next_smallest = None
    next_larger = None
    
    for i in lst:
        if next_smallest == None or i < next_smallest:
            next_smallest = i
        elif next_larger == None or i > next_larger:
            next_larger = i
    
    if next_smallest == next_larger:
        return None
    
    for i in lst:
        if i == next_smallest:
            return next_larger
        elif i == next_larger:
            return next_smallest
    
    return None
