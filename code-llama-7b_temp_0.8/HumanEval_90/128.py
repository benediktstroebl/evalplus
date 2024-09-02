
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
    if len(lst) <= 1:
        return None
    else:
        my_list = lst[1:]
        for i in lst:
            if i > lst[0]:
                my_list.remove(i)
        if len(my_list) > 0:
            return sorted(my_list)[0]
        else:
            return None
