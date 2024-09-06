
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
    # Sort the list
    lst = sorted(lst)
    
    # If the list has more than 2 elements
    if len(lst) > 2:
        # Return the 2nd smallest element
        return lst[1]
    
    # If the list has 2 elements
    elif len(lst) == 2:
        # Return the 2nd smallest element
        return lst[1]
    
    # If the list has 1 element
    elif len(lst) == 1:
        # Return None
        return None
    
    # If the list is empty
    else:
        # Return None
        return None
