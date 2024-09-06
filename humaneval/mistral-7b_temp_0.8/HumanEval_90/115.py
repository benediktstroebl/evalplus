
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

    if len(lst) == 1:
        return None

    # Convert to a set
    # Removes duplicates
    lst_set = set(lst)
    if len(lst_set) == 1:
        return None

    # Take first element from the set and remove it from the list
    # Sort the rest of the list
    # Return the first element of the sorted list
    return lst_set.pop()
