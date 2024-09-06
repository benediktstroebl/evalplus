
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
    
    n = len(lst)
    
    # find the minimum
    min_index = 0
    for i in range(n):
        if lst[i] < lst[min_index]:
            min_index = i
    
    # find the second minimum
    min_index_2 = None
    for i in range(n):
        if i != min_index and (min_index_2 is None or lst[i] < lst[min_index_2]):
            min_index_2 = i
    
    return None if min_index_2 is None else lst[min_index_2]
