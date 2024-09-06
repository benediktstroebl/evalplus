
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
    
    # put your code here
    # Make the first pass to find the smallest number
    small = lst[0]
    for i in lst:
        if i < small:
            small = i
    # Return None if the list has only one element
    if len(lst) == 1:
        return None
    # Make the second pass to find the second smallest
    second = lst[0]
    for j in lst:
        if j < second and j != small:
            second = j
    # Return None if there is no second smallest element
    if second == small:
        return None
    else:
        return second
    # return list[0] if len(list) == 1 else None
    
    # my code
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
