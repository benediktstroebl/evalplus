
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
    
    n = len(lst)
    
    # Base case
    if n < 2:
        return None
    
    # Recursively compare the first and the second smallest element
    # Return the second smallest if it is smaller than the first
    # Otherwise return the first element
    if lst[0] < lst[1]:
        return lst[1]
    else:
        return lst[0]
