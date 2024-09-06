
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
    if not lst:
        return None
    
    smallest = min(lst)
    second_smallest = None
    
    for item in lst:
        if item == smallest:
            continue
        
        if second_smallest is None or item < second_smallest:
            second_smallest = item
    
    return second_smallest
