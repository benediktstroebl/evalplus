
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

    min_el = min(lst)
    next_el = None
    for el in lst:
        if el > min_el:
            if next_el == None:
                next_el = el
            elif next_el > el:
                next_el = el
    return next_el
