
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
    # if list is empty, return None
    if len(lst) == 0:
        return None

    # find the smallest element in the list
    smallest = min(lst)
    # if the list has only one element, return None
    if len(lst) == 1:
        return None

    # find the second smallest element
    second_smallest = min(lst)
    # if the second smallest element is smaller than the smallest element, return None
    if second_smallest <= smallest:
        return None

    # return the second smallest element
    return second_smallest
