
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

    # Get the minimum value of the list
    minimum = min(lst)
    if lst.count(minimum) > 1:
        # If there are two or more values with the same minimum value, return None
        return None
    else:
        # Loop through the list and find the next smallest value
        for value in lst:
            if value < minimum:
                return value
        # If no next smallest value is found, return None
        return None

