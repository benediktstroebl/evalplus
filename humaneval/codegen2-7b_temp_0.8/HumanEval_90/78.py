
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
    if len(lst) == 1:
        return None
    
    n = len(lst)
    start = 0
    end = n - 1
    
    while start < end:
        mid = start + (end - start) // 2
        if lst[mid] < lst[mid + 1]:
            return lst[mid + 1]
        
        if lst[mid] > lst[mid + 1]:
            start = mid + 1
        else:
            end = mid
    return lst[
