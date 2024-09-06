
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
    n = len(lst)
    if n == 0 or n == 1:
        return None
    min_index = 1
    for i in range(1, n):
        if lst[i] < lst[min_index]:
            min_index = i
    return lst[min_index]
