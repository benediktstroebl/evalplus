
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
    
    if len(lst) == 1:
        return None

    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
            j += 1
        i += 1

    return lst[1] if len(lst) > 1 else None
