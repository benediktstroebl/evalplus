
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
    
    # Set min to the first element in the list
    min = lst[0]
    
    # set second_min to None
    second_min = None
    
    # Iterate through the list
    for i in lst:
        if i > min:
            if second_min is None or i < second_min:
                second_min = i
        else:
            if i > second_min:
                second_min = i
    return second_min
