
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

    min_1 = 99999999999
    min_2 = 99999999999
    for i in lst:
        if i <= min_1:
            min_2 = min_1
            min_1 = i
        elif i < min_2:
            min_2 = i
    
    return min_2
