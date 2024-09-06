
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
    # Use python's built-in sort function to sort the list in ascending order
    lst.sort()
    # Find the second element of the list
    second_element = lst[1]
    # If the list is empty, return None
    if not lst:
        return None
    # Return the second smallest element
    return second_element
