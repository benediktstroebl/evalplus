
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
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return None
    elif len(lst) == 2:
        return min(lst)
    elif len(lst) == 3:
        if min(lst) == lst[0]:
            return None
        elif min(lst) == lst[1]:
            return lst[2]
        else:
            return lst[1]
    elif len(lst) > 3:
        if min(lst) == lst[0]:
            return next_smallest(lst[1:])
        elif min(lst) == lst[1]:
            return next_smallest(lst[2:])
        elif min(lst) == lst[2]:
            return lst[3]
        else:
            return lst[1]

