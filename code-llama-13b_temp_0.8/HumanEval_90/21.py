
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
    if lst == []:
        return None
    
    lowest = lst[0]
    lowest_index = 0
    second_lowest = None
    second_lowest_index = None
    
    for i in range(len(lst)):
        if lst[i] < lowest:
            lowest = lst[i]
            lowest_index = i
            
    for i in range(len(lst)):
        if lst[i] < second_lowest and lst[i] != lowest:
            second_lowest = lst[i]
            second_lowest_index = i
            
    if second_lowest_index == None:
        return None
    
    return lst[second_lowest_index]
