
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
    else:
        first = lst[0]
        second = lst[1]
        for i in lst:
            if i < first:
                first = i
            elif i < second:
                second = i
        if second == first:
            return None
        else:
            return second

