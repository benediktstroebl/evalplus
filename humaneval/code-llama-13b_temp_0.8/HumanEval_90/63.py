
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
    if lst is None or len(lst) < 2:
        return None
    
    smallest = lst[0]
    second_smallest = None
    
    for n in lst[1:]:
        if n < smallest:
            second_smallest = smallest
            smallest = n
        elif second_smallest is None or n < second_smallest:
            second_smallest = n
    
    return second_smallest

