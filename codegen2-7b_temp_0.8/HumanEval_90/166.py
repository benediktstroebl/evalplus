
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
    new_lst = [i for i in lst if i not in [None, None]]
    if new_lst == []:
        return None
    elif len(new_lst) == 1:
        return None
    else:
        return sorted(new_lst)[1]
    
