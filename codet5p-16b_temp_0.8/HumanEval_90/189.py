
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
    min_index = 0
    max_index = 1
    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
        elif lst[i] > lst[max_index]:
            max_index = i
    if max_index == min_index:
        return None
    return lst[max_index]

