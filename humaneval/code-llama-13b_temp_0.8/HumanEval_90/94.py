
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
    small1 = float("inf")
    small2 = float("inf")
    for i in lst:
        if i < small1:
            small2 = small1
            small1 = i
        elif i < small2 and i != small1:
            small2 = i
    if small2 == float("inf"):
        return None
    return small2
