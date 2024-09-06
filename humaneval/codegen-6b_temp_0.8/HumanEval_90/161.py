
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
    
    # if the list is empty, return None
    if not lst:
        return None
    
    # if list only has one element, return it
    if len(lst) == 1:
        return lst[0]
    
    current_smallest = lst[0]
    
    for i in lst:
        if i < current_smallest:
            current_smallest = i
    
    # next smallest = None
    if current_smallest == lst[0]:
        return None
    
    # find index of current_smallest in lst
    index = lst.index(current_smallest)
    
    # remove current_smallest from lst
    removed_lst = lst[:index] + lst[index+1:]
    
    # assert that the resulting list does not contain duplicates
    assert len(set(removed_lst)) == len(removed_lst)
    
    # return the 2nd smallest element
    return lst[1]
