
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
    
    smallest_num = lst[0]
    smallest_indx = 0
    
    for indx, num in enumerate(lst):
        if num < smallest_num:
            smallest_num = num
            smallest_indx = indx
    
    return smallest_num, smallest_indx
