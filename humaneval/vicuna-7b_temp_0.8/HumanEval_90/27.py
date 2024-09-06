
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
    # sort the list
    lst = sorted(lst)
    # check if the first two elements are the same
    if lst[0] == lst[1]:
        return None
    # if not, check if the second element is the smallest
    elif lst[1] < lst[0]:
        return lst[1]
    else:
        return None