
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
    
    lowest_val = lst[0]
    lowest_index = 0
    
    for i in range(len(lst)):
        if lst[i] < lowest_val:
            lowest_val = lst[i]
            lowest_index = i
    
    if lowest_index == 0:
        return None
    
    second_lowest = lst[lowest_index]
    for i in range(len(lst)):
        if lst[i] < second_lowest and lst[i] > lowest_val:
            second_lowest = lst[i]
    
    return second_lowest
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
