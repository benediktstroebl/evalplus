
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
    if lst == []:
        return None
    smallest, second_smallest = sorted(lst)[0], None
    for x in lst:
        if x < smallest:
            second_smallest = smallest
            smallest = x
        elif x < second_smallest and x != smallest:
            second_smallest = x
    return second_smallest

