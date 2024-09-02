
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
    next_smallest = None
    if len(lst) < 2:
        return next_smallest

    # get the smallest number in the list
    lst.sort()
    smallest = lst[0]

    for i in lst:
        if i != smallest:
            next_smallest = i
            break

    return next_smallest
