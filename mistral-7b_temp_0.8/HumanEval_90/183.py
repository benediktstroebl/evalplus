
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
    if len(lst) == 1:
        return None
    elif len(lst) == 2:
        if lst[0] < lst[1]:
            return lst[1]
        else:
            return lst[0]
    else:
        n1 = lst[0]
        n2 = lst[1]
        for i in lst:
            if i < n1:
                n1 = i
            elif i < n2 and i > n1:
                n2 = i
        if n2 == None:
            return None
        return n2

