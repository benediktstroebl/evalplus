
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
    # Return None if list is empty
    if lst == []:
        return None
    # Set first item as the smallest
    smallest = lst[0]
    # Set second item as the next smallest
    next_smallest = lst[1] if len(lst) > 1 else None
    # Loop through list
    for i in lst[2:]:
        # If item is smaller than current smallest, set item as the smallest and then
        # set the next smallest to current smallest
        if i < smallest:
            next_smallest = smallest
            smallest = i
        # If item is smaller than current smallest, set item as next smallest
        elif i < next_smallest:
            next_smallest = i
    # Return next smallest
    return next_smallest
