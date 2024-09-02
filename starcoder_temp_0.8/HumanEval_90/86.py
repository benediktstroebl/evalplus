
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
    # return next_smallest([1, 2, 3, 4, 5]) == 2
    # return next_smallest([5, 1, 4, 3, 2]) == 2
    # return next_smallest([]) == None
    # return next_smallest([1, 1]) == None
    
    smallest = lst[0]
    second_smallest = None

    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]

    for i in range(1, len(lst)):
        if lst[i] < smallest and lst[i]!= smallest:
            second_smallest = lst[i]
            break

    return second_smallest

