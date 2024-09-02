
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
    # A set is an unordered collection with no duplicate elements
    # unordered means that you can't assume its items are sorted
    # no duplicate means that when you add an element to a set, it doesn't add the duplicates
    s = set(lst)
    
    # Set min_value to be the smallest value in the list
    min_value = min(s)
    
    # Remove the smallest value from the set
    s.remove(min_value)
    
    if len(s) == 0:
        return None
    
    # Return the smallest element in the set
    return min(s)
    
