
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

    if len(lst) < 2:
        return None

    my_set = set(lst)
    next_smallest = None
    while len(my_set) > 0:
        current_min = min(my_set)
        my_set.remove(current_min)
        if next_smallest is None:
            next_smallest = current_min
        else:
            if next_smallest > current_min:
                next_smallest = current_min

    return next_smallest
