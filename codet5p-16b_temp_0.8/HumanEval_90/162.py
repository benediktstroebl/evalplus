
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
    if len(lst) == 0:
        return None
    
    min_elem = lst[0]
    min_i = 0
    for i in range(len(lst)):
        if lst[i] < min_elem:
            min_elem = lst[i]
            min_i = i
    
    second_min = lst[0]
    second_min_i = 0
    for i in range(len(lst)):
        if i == min_i:
            continue
        elif lst[i] < second_min and lst[i] > min_elem:
            second_min = lst[i]
            second_min_i = i
    
    if second_min_i == min_i:
        return None
    else:
        return second_min
