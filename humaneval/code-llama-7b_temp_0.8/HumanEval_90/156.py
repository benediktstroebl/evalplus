
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
    
    low = high = mid = 0
    
    if lst[0] >= lst[1]:
        low = 1
        high = 0
    else:
        low = 0
        high = 1
        
    while low < len(lst) and high < len(lst):
        if lst[low] < lst[high]:
            low += 1
        elif lst[low] >= lst[high]:
            mid += 1
            high += 1
            
    if mid == len(lst) - 1:
        return None
    
    return lst[mid]
