
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
    small = lst[0]
    result = None
    
    for i in lst:
        if small < i:
            small = i
        elif small > i and result is None:
            result = i
        elif small > i and result is not None and result < i:
            result = i
    return result
