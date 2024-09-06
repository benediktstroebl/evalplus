
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
    if len(lst) == 1:
        return lst[0]
    
    smallest = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
    
    return smallest

print(next_smallest([3, 1, 1, 1, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
