
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
    if len(lst) < 2:
        return None
    return min(lst[1:])
    # first check if the len of the list is greater than 2 then pass the index 1 to the minimum
    # then we can return the next smallest number
    # or we can do this:
    # if len(lst) < 2:
    #     return None
    # else:
    #     return min(lst[1:])
    

