
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
    
    # Fill in the body of this function so that it returns the 2nd smallest element of the list.
    # Return None if there is no such element.
    
    for i in lst:
        if lst.count(i) == 1:
            return i
    for i in lst:
        if lst.count(i) == 2:
            return i
    return None
    # list.count(i) returns the number of times i appears in the list, so if the number of times i appears in the list is one, i is the 2nd smallest number.

