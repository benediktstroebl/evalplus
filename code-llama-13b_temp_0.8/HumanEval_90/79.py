
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
    if lst == []:
        return None
    
    # Check if there is only one element in the list
    if len(lst) == 1:
        return None
    
    # If there are at least two elements in the list
    # Get the smallest value in the list
    smallest = min(lst)
    
    # Remove all instances of the smallest value from the list
    # This leaves us with all the values greater than the smallest
    # Then we just get the smallest value from the list
    lst.remove(smallest)
    return min(lst)
    
