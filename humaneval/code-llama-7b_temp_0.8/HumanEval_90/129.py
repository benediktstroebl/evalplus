
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
    min_val = None
    second_min_val = None
    for i in range(len(lst)):
        if min_val is None or lst[i] < min_val:
            min_val = lst[i]
        if min_val is not None and (second_min_val is None or lst[i] < second_min_val):
            second_min_val = lst[i]

    return second_min_val
