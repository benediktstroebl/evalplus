
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
    # Check if the list is empty
    if not lst:
        return None
    
    # Keep track of the smallest element in the list
    min_element = lst[0]
    
    # Loop through the rest of the list
    for element in lst[1:]:
        # If the current element is smaller than the smallest element
        if element < min_element:
            # Update the smallest element to the current element
            min_element = element
    
    # Return the second smallest element (which should be the current smallest element)
    return min_element