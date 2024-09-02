
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
    for i in lst:
        if len(lst) == 1:
            return i
    if lst[0] < lst[1]:
        if len(lst) == 2:
            return lst[1]
        return lst[0]
    if lst[0] > lst[1]:
        if len(lst) == 2:
            return lst[0]
        return lst[1]
    if lst[1] < lst[2]:
        if len(lst) == 3:
            return lst[2]
        return lst[1]
    if lst[1] > lst[2]:
        if len(lst) == 3:
            return lst[1]
        return lst[2]
    if lst[2] < lst[3]:
        if len(lst) == 4:
            return lst[3]
        return lst[2]
    if lst[2] > lst[3]:
        if len(lst) == 4:
            return l
