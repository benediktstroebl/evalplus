
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
    second_min_val = lst[0]
    for i in lst:
        if i < min_val:
            second_min_val = min_val
            min_val = i
        elif i < second_min_val and i!= min_val:
            second_min_val = i
    return second_min_val

