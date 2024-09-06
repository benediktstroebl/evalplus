
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
    
    n1 = lst[0]
    n2 = lst[1]
    
    for i in range(2, len(lst)):
        if lst[i] < n1:
            n1 = lst[i]
        elif lst[i] < n2:
            n2 = lst[i]
    
    if n1 == n2:
        return None
    return n2
    
    
    
