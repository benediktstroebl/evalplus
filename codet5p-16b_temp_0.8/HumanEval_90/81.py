
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

    min_val = min(lst)
    min_val_index = lst.index(min_val)
    next_min = None
    for i in range(len(lst)):
        if i == min_val_index:
            continue
        if min_val_index < i:
            next_min = lst[i]
            break
        elif min_val_index > i:
            next_min = lst[i]
            break
    return next_min
