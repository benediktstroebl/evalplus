
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
    # none of the conditions are met
    # return the smaller number
    lst.sort()
    return lst[1]

    # init the first smallest number
    smallest = None
    # init the second smallest number
    second_smallest = None
    # iterate over the list
    for number in lst:
        # if the current number is smaller than the smallest number
        # or if there is no smallest number set, set the current number
        # to the smallest number
        if smallest is None or number < smallest:
            smallest = number
        # if the current number is smaller than the second smallest number
        # and smaller than the smallest number, set the current number
        # as the second smallest number
        elif second_smallest is None or number < second_smallest:
            second_smallest = number
    return second_smallest

