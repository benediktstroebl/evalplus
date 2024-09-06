
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
    if not lst:
        return None
    min_ = lst[0]
    min_idx = 0
    for i, v in enumerate(lst):
        if v < min_ and v != min_:
            min_ = v
            min_idx = i
    return min_ if min_idx < len(lst) - 1 else None

