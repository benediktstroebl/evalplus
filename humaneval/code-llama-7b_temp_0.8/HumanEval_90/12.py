
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
    #
    # Write your code here.
    #
    # how to handle an empty list?
    # how to handle a list with a single item?
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return None

    lst_sort = sorted(lst)
    lst_uniq = list(set(lst))

    # return lst_uniq[lst_uniq.index(lst_sort[1]) + 1]
    return lst_sort[1]

