
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
    
    min1, min2 = None, None
    for i in lst:
        if min1 == None or i < min1:
            min2 = min1
            min1 = i
        elif min2 == None or i < min2:
            min2 = i
    if min2 == None: return None
    return min2
