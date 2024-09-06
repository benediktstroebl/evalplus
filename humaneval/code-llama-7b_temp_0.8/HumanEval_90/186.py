
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

    min_val = lst[0]
    min_val_2 = lst[1]
    for i in lst:
        if min_val > i and min_val_2 > i:
            min_val_2 = i
    if min_val_2:
        return min_val_2
    else:
        return None

