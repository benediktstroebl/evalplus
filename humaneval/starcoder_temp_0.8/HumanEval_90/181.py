
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
    elif len(lst) == 1:
        return None
    elif len(lst) == 2:
        return lst[0] if lst[0] < lst[1] else lst[1]
    else:
        smaller = lst[0]
        small_i = 0
        for i in range(1, len(lst)):
            if lst[i] < smaller:
                smaller = lst[i]
                small_i = i
            if lst[i] > smaller:
                return smaller
            elif lst[i] == smaller and i < small_i:
                return smaller
        return smaller

