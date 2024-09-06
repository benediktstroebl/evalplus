
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
    list_copy = lst[:]
    min = max = list_copy[0]
    for el in list_copy:
        if el < min:
            min = el
    
    list_copy.remove(min)
    if len(list_copy) > 0:
        for el in list_copy:
            if el < max:
                max = el
        return max
    else:
        return None
