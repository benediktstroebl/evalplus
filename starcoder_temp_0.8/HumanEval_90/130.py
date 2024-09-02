
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
    # Fill in the conditionals
    # if the list is empty return None
    if lst == []:
        return None
    
    # if the list has 1 element return None
    if len(lst) == 1:
        return None
    
    # if the list has 2 elements
    # return the smallest element in the list
    if len(lst) == 2:
        return lst[0] if lst[0] < lst[1] else lst[1]
        
    # set the min to the first element in the list
    min = lst[0]
    
    # iterate through the rest of the list
    for item in lst[1:]:
        
        # if the item is smaller than the minimum
        # set the min to the item
        if item < min:
            min = item
    
    # set a variable to hold the first item in the list
    # then iterate through the rest of the list
    for item in lst[1:]:
        
        # if the item is equal to the min
        # return the second item in the list
        if item == min:
            return lst[lst.index(item) + 1]
    
    # return None if the list doesn't contain the min
    return None
    
    
