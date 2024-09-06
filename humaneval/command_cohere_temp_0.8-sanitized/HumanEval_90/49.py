def next_smallest(lst):
    """
    Returns the second smallest number in lst.
    Returns None if there is no second smallest number, i.e., if the list has less than two elements.
    """
    # Sort the list
    lst = sorted(lst)
    
    # If the list has less than two elements, return None
    if len(lst) < 2:
        return None
    
    # Return the second element in the sorted list
    return lst[1]