
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
    assert(lst)
    length = len(lst)
    if length < 2:
        return None
    else:
        lst.sort()
        if length < 3:
            return lst[1]
        else:
            for i in range(2, length):
                if lst[i-1]!= lst[i]:
                    return lst[i]
                else:
                    return None
