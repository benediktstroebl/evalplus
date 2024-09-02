
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
    min_index = 0
    for i, num in enumerate(lst):
        if num < lst[min_index]:
            min_index = i
    return lst[min_index+1] if min_index < len(lst)-1 else None
