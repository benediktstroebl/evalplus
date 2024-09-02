
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
    
    sort_list = lst[:]
    sort_list.sort()
    if len(sort_list) == 1:
        return None
    
    if sort_list[0] != sort_list[1]:
        return sort_list[1]
    else:
        for i in range(2, len(sort_list)):
            if sort_list[i] != sort_list[i - 1]:
                return sort_list[i]
        return None
        
