
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

    
    if len(lst) < 2:
        return None
    
    if lst[0] < lst[1]:
        min = lst[0]
        second_min = lst[1]
    else:
        min = lst[1]
        second_min = lst[0]
    
    for i in range(2, len(lst)):
        if lst[i] < min:
            second_min = min
            min = lst[i]
        elif lst[i] < second_min:
            second_min = lst[i]
    
    return second_min
