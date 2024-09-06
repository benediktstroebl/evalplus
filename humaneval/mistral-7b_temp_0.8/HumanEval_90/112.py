
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
    smallest_number = None
    second_smallest_number = None

    for x in lst:
        if smallest_number is None:
            smallest_number = x
        if x < smallest_number:
            smallest_number = x

        if smallest_number is None:
            second_smallest_number = x
        if x < smallest_number and x > second_smallest_number:
            second_smallest_number = x

    return second_smallest_number

