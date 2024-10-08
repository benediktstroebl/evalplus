
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
    n = len(lst)
    if n == 0:
        return None
    if n == 1:
        return None
    if n == 2:
        return lst[0] if lst[0] < lst[1] else lst[1]
    
    lst = sorted(lst)
    i = 0
    while i < n - 1:
        if lst[i] < lst[i+1]:
            return lst[i+1]
        else:
            i += 1
    return lst[n-1]
