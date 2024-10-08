
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
    if len(lst) == 2:
        return lst[1]

    first = lst[0]
    min_val = lst[1]
    for item in lst:
        if item < first:
            first = item
        if item < min_val and item > first:
            min_val = item

    return min_val
