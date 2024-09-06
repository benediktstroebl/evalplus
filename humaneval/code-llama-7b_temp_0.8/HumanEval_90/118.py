
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

    min_val = None
    second_min_val = None

    for i in lst:
        if min_val is None:
            min_val = i
            second_min_val = i
        else:
            if min_val > i and second_min_val > i:
                second_min_val = i
            elif i < min_val:
                second_min_val = min_val
                min_val = i

    if second_min_val == min_val:
        return None
    return second_min_val
