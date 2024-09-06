
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
    lst_len = len(lst)
    if lst_len == 0:
        return None
    min_ind = lst.index(min(lst))
    if min_ind == 0:
        return lst[1]
    elif min_ind == lst_len - 1:
        return lst[lst_len - 2]
    else:
        return lst[min_ind + 1]
