
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
    smallest = lst[0]
    next_smallest = lst[1]
    
    for i in lst[2:]:
        if i < smallest:
            next_smallest = smallest
            smallest = i
        elif i < next_smallest and i != smallest:
            next_smallest = i
    if next_smallest == smallest:
        return None
    return next_smallest

