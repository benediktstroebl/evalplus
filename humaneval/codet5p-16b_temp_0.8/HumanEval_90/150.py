
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
    lst2 = []
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            lst2.append(lst[i - 1])
    if len(lst2) < 2:
        return None
    return lst2[1]

