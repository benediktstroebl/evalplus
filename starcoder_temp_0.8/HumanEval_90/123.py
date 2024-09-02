
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
    second_smallest = None
    for x in lst:
        if smallest == None or x < smallest:
            smallest = x
            continue
        if second_smallest == None or x < second_smallest:
            second_smallest = x
    if smallest!= None and second_smallest!= None:
        return second_smallest
    return None
