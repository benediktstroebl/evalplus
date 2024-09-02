
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
    a = lst[0]
    b = lst[1]
    if a < b:
        a, b = b, a
    for i in range(2, len(lst)):
        if lst[i] > a:
            a = lst[i]
            continue
        if lst[i] < b:
            b = lst[i]
            continue
    if b == a:
        return None
    return b

