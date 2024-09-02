
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
    small = -1
    small_idx = -1
    for i, n in enumerate(lst):
        if small == -1 or n < small:
            small = n
            small_idx = i
    if small_idx == 0:
        return None
    else:
        return lst[small_idx - 1]
