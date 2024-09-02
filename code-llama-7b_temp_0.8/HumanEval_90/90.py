
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

    min_val = min(lst)

    if lst.count(min_val) == 1:
        return min(lst[lst.index(min_val) + 1:])
    else:
        return min(x for x in lst if x > min_val)

