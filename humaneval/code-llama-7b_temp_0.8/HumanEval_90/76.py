
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
    if not lst or len(lst) < 2:
        return None

    if len(lst) == 2:
        return lst[0] if lst[1] <= lst[0] else lst[1]

    minimum = lst[0]
    minimum_counter = 1
    for i in range(1, len(lst)):
        if lst[i] < minimum:
            minimum = lst[i]
            minimum_counter = 1
        elif lst[i] == minimum:
            minimum_counter += 1
    
    if minimum_counter > 1:
        return minimum
    
    for i in range(1, len(lst)):
        if lst[i] < lst[0]:
            return lst[i]
    
    return None

