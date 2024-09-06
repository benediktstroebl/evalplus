
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
    
    min_index = min(range(len(lst)), key=lst.__getitem__)
    min_value = lst[min_index]
    
    second_smallest_index = None
    for i in range(len(lst)):
        if lst[i] < min_value:
            second_smallest_index = i
    if second_smallest_index == None:
        return None
    else:
        return lst[second_smallest_index]
