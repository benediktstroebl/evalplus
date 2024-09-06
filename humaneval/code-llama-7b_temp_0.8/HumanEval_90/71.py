
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

    if not lst:
        return None

    smallest = lst[0]
    second_smallest = None

    for element in lst:
        if element < smallest:
            smallest, second_smallest = element, smallest
        elif element < second_smallest:
            second_smallest = element

    return second_smallest

