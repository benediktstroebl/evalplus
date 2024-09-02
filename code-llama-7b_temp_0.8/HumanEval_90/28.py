
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
    if len(lst) == 0:
        return None
    smallest = lst[0]
    next_smallest_index = None
    for i, n in enumerate(lst):
        if n < smallest:
            smallest = n
            next_smallest_index = i
    if next_smallest_index == 0:
        return None
    return lst[next_smallest_index - 1]































