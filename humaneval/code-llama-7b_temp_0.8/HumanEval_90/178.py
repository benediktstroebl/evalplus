
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

    next_smallest = None
    smallest_element = None

    if len(lst) == 1:
        return next_smallest

    for element in lst:
        if smallest_element is None or element < smallest_element:
            smallest_element = element

    for element in lst:
        if smallest_element is not None and next_smallest is None and element > smallest_element:
            next_smallest = element
        elif smallest_element is not None and element > smallest_element and element < next_smallest:
            next_smallest = element

    return next_smallest
