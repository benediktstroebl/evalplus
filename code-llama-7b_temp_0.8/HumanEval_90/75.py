
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
    for elem in lst:
        if smallest == None or elem < smallest:
            smallest = elem
    if len(lst) < 2:
        return None
    else:
        smallest2 = None
        for elem in lst:
            if elem > smallest and (smallest2 == None or elem < smallest2):
                smallest2 = elem
        return smallest2
