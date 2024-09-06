
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
    
    min1 = float('inf')
    min2 = float('inf')
    
    for num in lst:
        if num < min1:
            min1, min2 = num, min1
        elif num < min2 and num > min1:
            min2 = num
    
    return min2 if min2 < float('inf') else None
