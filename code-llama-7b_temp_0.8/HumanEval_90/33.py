
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
    min_value = None
    min_count = 0
    for i in lst:
        if i < min_value or min_value == None:
            min_value = i
            min_count = 1
        elif i == min_value:
            min_count += 1
        else:
            if min_count == 1:
                min_value = i
                min_count = 1
            else:
                continue
    if min_count > 1:
        return min_value
    else:
        return None
