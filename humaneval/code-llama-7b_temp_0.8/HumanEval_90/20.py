
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
    first = None
    second = None
    for num in lst:
        if first is None:
            first = num
        elif num < first:
            second = first
            first = num
        elif second is None:
            second = num
        elif num < second:
            second = num
    return second

