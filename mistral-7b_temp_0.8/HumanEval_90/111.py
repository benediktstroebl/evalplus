
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
    if len(lst) == 1:
        return None
    if len(lst) == 2:
        if lst[0] == lst[1]:
            return None
        else:
            return min(lst)
    # create a copy of the list
    lst_cpy = lst[:]
    # find the smallest element in the list
    min_elem = min(lst)
    # remove the smallest element from the list
    lst_cpy.remove(min_elem)
    # return the 2nd smallest element or None if the list is empty or has only one element
    if len(lst_cpy) == 0:
        return None
    elif len(lst_cpy) == 1:
        return lst_cpy[0]
    else:
        return min(lst_cpy)
