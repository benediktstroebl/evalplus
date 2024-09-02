
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
    
    new_list = []
    for i in range(len(lst)):
        if len(new_list) == 0 or lst[i] < new_list[0]:
            new_list.insert(0,lst[i])
        else:
            new_list.append(lst[i])
    
    
    return new_
