
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
    if len(lst) == 0:
        return None
    # Select the first item as the smallest number
    current_smallest = lst[0]
    
    # Iterate through the list
    for i in lst:
        # Check if current item is smaller than the current smallest item
        if i < current_smallest:
            # If so, update the current smallest item to be the current item
            current_smallest = i
            
    # Keep iterating through the list
    for i in lst:
        # Check if current item is smaller than the current smallest item
        if i < current_smallest:
            # If so, update the current smallest item to be the current item
            current_smallest = i
            
    # Return the second smallest number, if it exists
    return current_smallest
