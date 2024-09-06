
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

    # Check if the list has two or more elements
    if len(lst) >= 2:

        # Sort the list and return the second element
        lst.sort()
        return lst[1]

    # The list has one element
    return None

