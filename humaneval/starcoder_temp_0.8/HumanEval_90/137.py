
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
    smallest = lst[0]
    next_smallest = None
    for num in lst:
        if num < smallest:
            next_smallest = smallest
            smallest = num
        elif num > smallest and next_smallest is None:
            next_smallest = num
        elif num < next_smallest:
            next_smallest = num
    return next_smallest
