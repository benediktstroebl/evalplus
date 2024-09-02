
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

    # Bottle-neck: if the list is very small or very large this can be slow.
    # If a list has duplicate values the duplicated items must be accounted for.
    # This means you cannot rely on min() or max()
    if not lst or len(lst) == 1:
        return None
    
    if len(lst) == 2:
        return None if lst[0] == lst[1] else min(lst)
    
    lst = sorted(lst)
    for i, val in enumerate(lst):
        if i < 1:
            continue
        if val != lst[i-1]:
            return lst[i-1]
    return None
    
