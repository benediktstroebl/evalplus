
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
    # Check if the list is empty
    if not lst:
        return None

    # If the list is not empty,
    # find the smallest element of the list
    smallest = lst[0]
    for item in lst[1:]:
        if item < smallest:
            smallest = item

    # If the smallest element is not the first element of the list,
    # return the second smallest element as it's not possible to have a smaller one
    if smallest != lst[0]:
        return lst[1]
    else:
        return smallest
