
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
    list_size = len(lst)
    if list_size < 2:
        return None
    i = 0
    lowest = 0
    while i < list_size:
        current = lst[i]
        i += 1
        if current < lowest:
            lowest = current
        if current > lowest:
            return lowest

