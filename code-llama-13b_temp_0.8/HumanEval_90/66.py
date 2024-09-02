
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
    
    min_val = float('inf')
    min_idx = 0
    second_min_idx = 0
    second_min_val = float('inf')
    
    for i, val in enumerate(lst):
        if val < min_val:
            min_idx = i
            min_val = val
            
        if second_min_val > val > min_val:
            second_min_val = val
            second_min_idx = i
            
    return None if second_min_val == float('inf') else lst[second_min_idx]

